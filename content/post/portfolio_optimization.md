---
title: "Portfolio Optimization: Beyond Markowitz with Denoising"
date: 2026-02-01
summary: "Improving mean-variance optimization using covariance denoising (Ledoit-Wolf, Marchenko–Pastur, EPO, Bayesian), hierarchical clustering (HRP, HERC), and combinatorial purged cross-validation."
tags: ["Quantitative Finance", "Portfolio Management", "Machine Learning"]
categories: [Quantitative Finance]
math: true
---

The classical Markowitz Mean-Variance Optimization (MVO) remains one of the most influential frameworks in portfolio management. However, its practical application is plagued by estimation error in the covariance matrix, sensitivity to inputs, and a tendency to produce concentrated, unstable portfolios. In this post we explore three families of techniques — denoising, clustering, and back-testing — that address these limitations, and show how combining them can yield more robust, diversified portfolios.

We illustrate the ideas on a multi-stock universe spanning several sectors, using daily returns over a recent historical window split into training and testing periods.

---

## 1. Baseline: Markowitz MVO

The traditional MVO solves for the portfolio weights \\(\mathbf{w}^{*}\\) that maximise the Sharpe ratio:

$$\mathbf{w}^{*} = \underset{\mathbf{w}}{\operatorname{argmax}} \; \frac{\mathbf{w}^{\top} \mu}{\sqrt{\mathbf{w}^{\top} \Sigma \mathbf{w}}}$$

subject to \\(\mathbf{w} \geq 0\\), \\(\sum w\_{i} = 1\\).

The efficient frontier traces all optimal risk-return trade-offs, but the weights that land on it are notoriously sensitive to small perturbations in \\(\Sigma\\). Even minor changes in the estimated covariance can produce wildly different allocations.

---

## 2. Denoising the Covariance Matrix

The covariance matrix \\(\Sigma\\) is the central weakness of MVO. With \\(N\\) assets the number of parameters grows as \\(O(N^{2})\\), and sampling noise accumulates fast, especially when the sample size \\(T\\) is not much larger than \\(N\\). Because MVO inverts \\(\Sigma\\), tiny noisy eigenvalues get amplified into large, erratic weight swings.

### 2.1 Ledoit-Wolf Shrinkage

The Ledoit-Wolf (LW) estimator replaces the sample covariance with a convex combination:

$$\Sigma\_{\mathrm{shrunk}} = (1 - \alpha) S + \alpha T$$

where \\(S\\) is the sample covariance, \\(T\\) is a structured target (typically a diagonal matrix of sample variances), and \\(\alpha\\) is chosen to minimise the expected Frobenius loss against the true covariance.

The LW method shrinks all correlations uniformly toward zero, reducing noise without dramatically altering the portfolio structure.

### 2.2 Enhanced Portfolio Optimization (EPO)

EPO controls the tension between a fully data-driven portfolio and a maximally diversified one through a single shrinkage parameter \\(w \in [0, 1]\\). Rather than denoising the covariance matrix in eigenvalue space, EPO acts directly on the off-diagonal correlations, blending the historical covariance with a diagonal target:

$$\tilde{\Sigma} = (1 - w)\,\Sigma\_{\mathrm{hist}} + w\,\Sigma\_{\mathrm{target}}$$

Here \\(\Sigma\_{\mathrm{hist}}\\) is the sample covariance carrying all historical correlations, while \\(\Sigma\_{\mathrm{target}}\\) retains only the diagonal variances — setting every cross-asset covariance to zero. As \\(w\\) increases from 0 to 1, the optimizer progressively ignores inter-asset correlations, transitioning the solution from a concentrated MVO portfolio toward a signal-weighted diversified one.

In its simplest form (Simple EPO), this shrinkage has a transparent closed-form interpretation. The resulting weight vector decomposes as a convex combination of two portfolios:

$$\mathbf{w}\_{\mathrm{EPO}} = (1 - w)\,\mathbf{w}\_{\mathrm{MVO}} + w\,\mathbf{w}\_{\mathrm{signal}}$$

where \\(\mathbf{w}\_{\mathrm{MVO}}\\) are the classical mean-variance weights (sensitive to noisy correlations in \\(\Sigma\_{\mathrm{hist}}\\)) and \\(\mathbf{w}\_{\mathrm{signal}}\\) are signal-only weights derived from expected returns alone, ignoring cross-asset structure entirely. The parameter \\(w\\) thus provides a direct, interpretable dial between estimation-risk-heavy MVO and a pure-signal allocation.

### 2.3 Marchenko–Pastur Denoising

Random Matrix Theory (RMT) offers a more surgical approach to denoising. The key insight is that when \\(T\\) observations of \\(N\\) asset returns are drawn from a true covariance matrix \\(\Sigma\\), the eigenvalues of the sample covariance \\(S\\) are systematically distorted. If the returns were purely random (i.e., \\(\Sigma = I\\)), the eigenvalue density of \\(S\\) would follow the **Marchenko–Pastur distribution**:

$$f\_{\mathrm{MP}}(\lambda) = \frac{T}{2 \pi \sigma^{2} N} \frac{\sqrt{(\lambda\_{+} - \lambda)(\lambda - \lambda\_{-})}}{\lambda}$$

for \\(\lambda \in [\lambda\_{-},\; \lambda\_{+}]\\), where the bounds are:

$$\lambda\_{\pm} = \sigma^{2} \left(1 \pm \sqrt{\frac{N}{T}}\right)^{2}$$

and \\(\sigma^{2}\\) is the variance of the noise. Eigenvalues that fall within \\([\lambda\_{-},\; \lambda\_{+}]\\) are consistent with pure randomness — they carry no genuine signal. Eigenvalues above \\(\lambda\_{+}\\) reflect true structure in the data: sector exposures, market factors, and other real correlations.

The denoising procedure works as follows:

1. **Compute the eigendecomposition** of the sample correlation matrix: \\(C = Q \Lambda Q^{\top}\\).
2. **Fit the Marchenko–Pastur distribution** to the bulk of eigenvalues to estimate \\(\sigma^{2}\\) (the noise variance) and identify the threshold \\(\lambda\_{+}\\).
3. **Shrink the noisy eigenvalues.** All eigenvalues \\(\lambda\_{i} \leq \lambda\_{+}\\) are replaced. The simplest approach sets them all equal to their average, preserving the matrix trace:

$$\tilde{\lambda}\_{i} = \frac{1}{\lvert \mathcal{N} \rvert} \sum\_{j \in \mathcal{N}} \lambda\_{j} \qquad \text{for } i \in \mathcal{N}$$

where \\(\mathcal{N} = \\{i : \lambda\_{i} \leq \lambda\_{+}\\}\\). The signal eigenvalues (\\(\lambda\_{i} > \lambda\_{+}\\)) are left untouched.

4. **Reconstruct** the denoised correlation matrix: \\(\tilde{C} = Q \tilde{\Lambda} Q^{\top}\\).

The ratio \\(q = N / T\\) is critical: the higher it is, the wider the Marchenko–Pastur bulk and the more eigenvalues are noise-dominated. For a typical portfolio with \\(N = 12\\) stocks and \\(T \approx 390\\) daily observations, \\(q \approx 0.03\\), meaning the noise band is relatively narrow and most eigenvalues carry signal. But for larger universes say \\(N = 500\\) with a year of daily data \\(q\\) exceeds 1 and the majority of eigenvalues are pure noise. This is precisely where RMT denoising is useful.

Compared to Ledoit-Wolf shrinkage, which applies a uniform correction to every element of \\(\Sigma\\), the Marchenko–Pastur approach is **selective**: it leaves the dominant eigenvectors (market, sector, and style factors) intact while collapsing the noisy directions. This surgical precision makes it particularly effective for large portfolios where the signal-to-noise separation is stark.

### 2.4 Bayesian Approaches

The Bayesian framework treats \\(\mu\\), \\(\Sigma\\), and the weights \\(\mathbf{w}\\) as random variables, naturally incorporating parameter uncertainty:

- **Priors:** Normal for mean returns; Half-Normal for volatilities; \\(\mathrm{LKJ}(\eta = 2)\\) for the correlation matrix (encouraging shrinkage toward independence); Dirichlet for weights (ensuring they sum to one and lie in \\([0, 1]\\)).
- **Constraints and objectives** (weight caps, Sharpe maximisation) are encoded as potential functions in the MCMC sampler, making parameter estimation and portfolio construction a single unified step.

In practice, the Bayesian Normal model substantially outperforms the baseline across Sharpe ratio, drawdown, and volatility. Two factors drive this:

1. **Joint uncertainty propagation** — correlated errors in \\(\mu\\) and \\(\Sigma\\) cancel rather than compound.
2. **Posterior averaging** — the final weights are an expectation over thousands of MCMC draws, smoothing out any single noisy optimum.

The Student-\\(t\\) variant adds robustness to fat-tailed returns, trading a little Sharpe for improved tail-risk control (lower VaR).

---

## 3. Clustering: Hierarchical Risk Parity and Beyond

Rather than inverting \\(\Sigma\\), clustering methods allocate capital through the hierarchical structure of asset correlations.

### 3.1 Hierarchical Risk Parity (HRP)

HRP follows three steps:

1. **Hierarchical clustering** — build a dendrogram from correlation-based distances using Ward linkage.
2. **Quasi-diagonalisation** — reorder \\(\Sigma\\) so correlated assets sit adjacent.
3. **Recursive bisection** — split the ordered assets top-down; at each split allocate inversely to each sub-cluster's variance:

$$w\_{L} = 1 - \frac{V\_{L}}{V\_{L} + V\_{R}}, \qquad w\_{R} = 1 - w\_{L}$$

where \\(V\_{L}\\) and \\(V\_{R}\\) are the inverse-variance-weighted portfolio variances of the left and right splits.

HRP avoids matrix inversion entirely, scales well, and naturally diversifies across clusters. In out-of-sample testing it consistently outperforms baseline MVO on risk-adjusted returns.

### 3.2 Hierarchical Equal Risk Contribution (HERC)

HERC extends HRP with two refinements:

- **Early stopping** via a Gap Index selects the optimal number of clusters, preventing overfitting to noisy sub-clusters.
- **Risk-aware allocation** uses Conditional Drawdown-at-Risk (CDaR) instead of variance, capturing tail risk:

$$\operatorname{CDaR}\_{\alpha}(\mathbf{w}) = \frac{1}{1 - \alpha} \int\_{\alpha}^{1} D\_{q}(\mathbf{w}) \, dq$$

where \\(D\_{q}\\) is the portfolio drawdown at quantile \\(q\\).

HERC tends to achieve the strongest risk-adjusted returns among the methods studied, with improved diversification across sectors, though at marginally higher tail risk.

---

## 4. Back-testing with CPCV

Standard train/test splits waste data and can introduce look-ahead bias. Combinatorial Purged Cross-Validation (CPCV) partitions the time series into \\(G\\) groups and selects \\(K\\) groups for testing, generating \\(\binom{G}{K}\\) paths while:

- **Purging** observations near the train/test boundary to prevent information leakage.
- Preserving temporal ordering within each path.

With \\(G = 5\\) and \\(K = 2\\), CPCV produces 10 independent evaluation paths, giving a far richer picture of out-of-sample behaviour than a single train/test split.

---

## 5. Combining Techniques

The real power emerges from composition:

- **Denoising + Back-testing (EPO + CPCV):** CPCV searches over shrinkage parameters and selects the median optimal \\(\alpha\\) across paths, providing a stable, data-driven covariance estimate. This yields consistent incremental gains over standalone denoising.
- **Clustering + Back-testing (HRP/HERC + CPCV):** Clustering methods are sensitive to the quality of the hierarchical structure in each fold. Folds with weak or unstable clusters can degrade performance. Increasing fold size or sampling frequency mitigates this.
- **Denoising + Clustering:** A denoised correlation matrix feeds cleaner distances into the hierarchical clustering step, producing more stable dendrograms and, consequently, more robust weight allocations.

[Read more →](https://github.com/SboneloMdluli/Financial-Engineering-Forum-Posts/blob/master/portfolio_optimization.ipynb)
