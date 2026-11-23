import torch
import torch.nn as nn


class MultiHeadCausalSelfAttention(nn.Module):
    def __init__(self, d_in, d_out, context_length, dropout, num_heads, qkv_bias=False):
        super().__init__()

        # Divide the total output features evenly among the heads.
        assert d_out % num_heads == 0

        self.num_heads = num_heads
        self.head_dim = d_out // num_heads

        # Project inputs into the combined Query, Key and Value representations.
        self.W_query = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_key = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_value = nn.Linear(d_in, d_out, bias=qkv_bias)

        # Combine the information produced by all heads.
        self.out_proj = nn.Linear(d_out, d_out, bias=qkv_bias)

        self.dropout = nn.Dropout(dropout)

        # Mark future-token positions that causal attention must block.
        mask = torch.triu(
            torch.ones(context_length, context_length),
            diagonal=1
        )

        # Keep the mask with the model, but not as a trainable parameter.
        self.register_buffer("mask", mask)

    def forward(self, x):
        # Input shape: (batch_size, sequence_length, input_features)
        batch_size, sequence_length, _ = x.shape

        # Step 1: Project the input into Q, K, and V.
        queries = self.W_query(x)
        keys = self.W_key(x)
        values = self.W_value(x)

        # Step 2: Split the features into separate heads.
        # Shape becomes (B, T, H, head_dim).
        queries = queries.view(
            batch_size, sequence_length, self.num_heads, self.head_dim
        )
        keys = keys.view(
            batch_size, sequence_length, self.num_heads, self.head_dim
        )
        values = values.view(
            batch_size, sequence_length, self.num_heads, self.head_dim
        )

        # Step 3: Arrange dimensions for attention calculations.
        # Shape becomes (B, H, T, head_dim).
        queries = queries.transpose(1, 2)
        keys = keys.transpose(1, 2)
        values = values.transpose(1, 2)

        # Step 4: Calculate attention scores independently for each head.
        # keys.transpose(2, 3) changes (B, H, T, head_dim)
        # into (B, H, head_dim, T)
        attention_scores = queries @ keys.transpose(2, 3)

        # Scale using the dimension of each head.
        attention_scores = attention_scores / (self.head_dim ** 0.5)

        # Step 5: Prevent each token from attending to future tokens.
        attention_scores = attention_scores.masked_fill(
            self.mask[:sequence_length, :sequence_length].bool(),
            -torch.inf
        )

        # Step 6: Convert scores into attention weights.
        attention_weights = torch.softmax(attention_scores, dim=-1)

        # Apply dropout to the attention weights during training.
        attention_weights = self.dropout(attention_weights)

        # Step 7: Retrieve weighted Valie information for each head.
        # Shape: (B, H, T, head_dim).
        context = attention_weights @ values

        # Step 8: Put the sequence dimension before the head dimension.
        # Shape: (B, T, H, head_dim)
        context = context.transpose(1, 2).contiguous()

        # Join the head features into one representation per token.
        # Shape: (B, T, d_out).
        context = context.view(batch_size, sequence_length, -1)

        # Step 9: Allow the model to mix information across heads.
        output = self.out_proj(context)

        return output


if __name__ == "__main__":
    ...