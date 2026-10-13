
import numpy as np

np.set_printoptions(precision=3, suppress=True)

# Sentence: "she reads books"
tokens = ["she", "reads", "books"]

# Each row represents a word embedding
X = np.array([
    [1.0, 0.3, 0.1, 0.0],  # she
    [0.2, 1.0, 0.2, 0.1],  # reads
    [0.9, 0.2, 0.1, 0.0]   # books
])

# Positional encoding for positions 0, 1, and 2
P = np.array([
    [0.0, 0.0, 0.0, 0.0],
    [0.4, 0.3, 0.2, 0.1],
    [0.8, 0.6, 0.4, 0.2]
])

# Reverse the word order
perm = [2, 1, 0]

# Clean target signal for diffusion
x_clean = np.array([
    0.1, 0.3, 0.5, 0.7,
    0.9, 0.7, 0.5, 0.3,
    0.1, -0.1, -0.3, -0.5,
    -0.3, -0.1, 0.1, 0.3
])

rng = np.random.default_rng(0)


def mse(a, b):
    return float(np.mean((a - b) ** 2))


# ==================================================
# TODO 1: Softmax and Attention
# ==================================================

def softmax(v):
    v = v - np.max(v)
    exp_v = np.exp(v)
    return exp_v / np.sum(exp_v)


def attention(M):
    scores = M @ M.T

    # Apply softmax independently to each row
    W = np.array([softmax(row) for row in scores])

    # Weighted combination of the input embeddings
    out = W @ M

    return out, W


out, W = attention(X)

print("Weight grid W:\n", W)
print("Row sums:", W.sum(axis=1))


# ==================================================
# TODO 2: Find the most-attended word
# ==================================================

for i, word in enumerate(tokens):
    j = np.argmax(W[i])
    print(f"{word} -> {tokens[j]} (weight: {W[i, j]:.3f})")

print("Every row sums to 1:", np.allclose(W.sum(axis=1), 1))


# ==================================================
# TODO 3: Test order blindness and positional encoding
# ==================================================

out_X, _ = attention(X)
out_perm, _ = attention(X[perm])

check1 = np.allclose(out_perm, out_X[perm])

out_XP, _ = attention(X + P)
out_permP, _ = attention(X[perm] + P)

check2 = np.allclose(out_permP, out_XP[perm])

print("Order-blind without positions:", check1)
print("Still order-blind with positions:", check2)


# ==================================================
# TODO 4: Diffusion denoising
# ==================================================

def denoise(steps, alpha=0.1):
    x = rng.normal(size=x_clean.shape)
    errors = [mse(x, x_clean)]

    for _ in range(steps):
        x = x + alpha * (x_clean - x)
        errors.append(mse(x, x_clean))

    return errors


errors = denoise(50, alpha=0.1)

print(
    "start:", round(errors[0], 4),
    "| after 1:", round(errors[1], 4),
    "| midway:", round(errors[25], 4),
    "| end:", round(errors[-1], 4)
)

print(
    "Final error with only 5 steps:",
    round(denoise(5, alpha=0.1)[-1], 4)
)
