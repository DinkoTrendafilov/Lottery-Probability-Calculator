Lottery Probability Calculator

A Python implementation of the hypergeometric distribution for calculating exact lottery probabilities.


📊 Overview

This tool calculates the exact probability distribution for lottery games using combinatorial mathematics. It's perfect for analyzing games like 6/49, where you need to understand your real chances of winning.
🎯 Features

    Hypergeometric Distribution: Calculates exact probabilities using combinatorial formulas

    Numerical Stability: Uses logarithms to prevent overflow with large numbers

    Complete Statistics: Provides mean, variance, and standard deviation

    Clean Output: Well-formatted results with probabilities, cumulative probabilities, and odds

🧮 Mathematical Model

The calculator uses the hypergeometric probability mass function:
text

P(X = k) = [C(K, k) × C(N-K, n-k)] / C(N, n)

Where:

    N = Total balls in lottery machine (49)

    K = Numbers marked on ticket (6)

    n = Numbers drawn in lottery (6)

    k = Number of matching numbers

    C(a, b) = Combinations of a choose b

🚀 Usage

Simply run the Python script:
bash

python lottery_probability.py

📈 Sample Output

Matches: 0 -- Probability: 43.5965% | Cumulative: 43.5965% | 1 From 2.3 cases
Matches: 1 -- Probability: 41.3019% | Cumulative: 84.8984% | 1 From 2.4 cases
Matches: 2 -- Probability: 13.2378% | Cumulative: 98.1362% | 1 From 7.6 cases
Matches: 3 -- Probability: 1.7650% | Cumulative: 99.9013% | 1 From 56.7 cases
Matches: 4 -- Probability: 0.0969% | Cumulative: 99.9981% | 1 From 1_032.4 cases
Matches: 5 -- Probability: 0.0018% | Cumulative: 100.0000% | 1 From 54_200.8 cases
Matches: 6 -- Probability: 0.0000% | Cumulative: 100.0000% | 1 From 13_983_816.0 cases

Statistics: 
Average value (μ): 0.7347
Variance (σ²): 0.5776
Standard deviation (σ): 0.7600


🔢 Key Results

    Most likely outcome: 0 or 1 match (85% combined probability)

    Probability of winning (3+ matches): 1.8638%

    Expected number of matches: 0.7347

    Jackpot odds: 1 in 13,983,816

🛠️ Technical Details

    Language: Python 3.6+

    Dependencies: None (uses only standard library)

    Memory: O(1) space complexity

    Time: O(n) time complexity

📚 Applications

    Educational Tool: Learn probability theory with real-world examples

    Lottery Analysis: Understand actual winning probabilities

    Statistical Modeling: Example of hypergeometric distribution implementation

    Decision Making: Informed analysis for lottery participation

🤝 Contributing

Feel free to fork the repository and submit pull requests for:

    Additional lottery formats

    Visualization features

    Enhanced statistical analysis

    Performance optimizations

📄 License

MIT License - free for educational and personal use.

Disclaimer: This tool is for educational purposes only. Gambling involves risk and should be approached responsibly.
