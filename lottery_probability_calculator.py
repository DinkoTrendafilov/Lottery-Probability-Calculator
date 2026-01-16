from math import comb, log, exp
from collections import defaultdict

# Hypergeometric distribution parameters for 6/49 lottery
N = 49  # Total number of balls in the urn
K = 6  # Number of winning balls (numbers we marked)
n = 6  # Number of balls drawn in the lottery

print("-" * 104)

probabilities = defaultdict(float)

cumulative = 0
for k in range(min(K, n) + 1):
    log_probability = log(comb(K, k)) + log(comb(N - K, n - k)) - log(comb(N, n))
    prob = exp(log_probability)
    probabilities[k] = prob
    cumulative += prob
    print(f"Matches: {k} -- Probability: {prob:.4%} | Cumulative: {cumulative:.4%} | 1 From {1 / prob:_.1f} cases")

mean = sum(k * prob for (k, prob) in probabilities.items())
variance = sum((k - mean) ** 2 * prob for (k, prob) in probabilities.items())
std_dev = variance ** 0.5

print("-" * 104)

print("Statistics: ")
print(f"Average value (μ): {mean:.4f}")
print(f"Variance (σ²): {variance:.4f}")
print(f"Standard deviation (σ): {std_dev:.4f}")

print("-" * 104)
