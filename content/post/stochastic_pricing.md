---
title: "Stochastic Pricing Models"
date: 2025-05-10
summary: "This article provides an exposition of stochastic models for option pricing, focusing on the mathematical formulation and computational techniques underlying the Heston and Merton jump-diffusion frameworks. Analytical and simulation-based approaches for pricing, risk management, and sensitivity analysis are discussed in detail."
tags: ["Options Pricing", "Quantitative Finance"]
categories: [Finance, Quantitative]
math: true
---

# Stochastic Pricing Models

This post presents the theoretical foundations of stochastic models for option pricing. We outline the mathematical structure and computational methods for European and American options under both the Heston and Merton jump-diffusion models, including the calculation of Greeks and barrier options.

## 1. Introduction to Stochastic Option Pricing

Stochastic models are essential for capturing the randomness in financial markets, especially for pricing derivatives like options. Two widely used models are:

- **Heston Model**: Incorporates stochastic volatility, allowing volatility to evolve randomly over time.
- **Merton Jump Diffusion Model**: Extends the Black-Scholes framework by adding random jumps in asset prices, capturing sudden market moves.

## 2. Heston Model

The Heston model describes the evolution of an asset price $S_t$ and its variance $v_t$ as:

\begin{equation*}
dS_t = \mu S_t dt + \sqrt{v_t}\ S_t\ dW_t^S
\end{equation*}

\begin{equation*}
dv_t = \kappa (\theta - v_t) dt + \sigma \sqrt{v_t}\ dW_t^v
\end{equation*}

where $dW_t^S$ and $dW_t^v$ are correlated Brownian motions.

\begin{equation*}
dW_t^S dW_t^v = \rho dt
\end{equation*}

Simulation of the Heston model involves generating correlated random walks for price and variance, and pricing options via Monte Carlo and Least Squares Monte Carlo (LSMC) methods. LSMC is used for American options, regressing future payoffs to estimate optimal early exercise.

In the Heston model, the two Brownian motions $dW_t^S$ and $dW_t^v$ are correlated with correlation coefficient $\rho$. To simulate these correlated processes using independent standard normal variables, we use the Cholesky decomposition.

Let $Z_1$ and $Z_2$ be independent standard normal random variables. The correlated Brownian increments can be constructed as:

\begin{equation*}
dW_t^S = \sqrt{dt}\ Z_1
\end{equation*}

\begin{equation*}
dW_t^v = \rho \sqrt{dt}\ Z_1 + \sqrt{1-\rho^2}\ \sqrt{dt}\ Z_2
\end{equation*}

This transformation ensures that $dW_t^S$ and $dW_t^v$ have the desired correlation $\rho$.

The Cholesky decomposition is used to decompose the covariance matrix of the Brownian motions, allowing us to generate correlated random variables from independent ones. For a $2 \times 2$ covariance matrix:

$$
\Sigma = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}
$$

The Cholesky factor $L$ is:

$$
L = \begin{pmatrix} 1 & 0 \\ \rho & \sqrt{1-\rho^2} \end{pmatrix}
$$

Given $\mathbf{Z} = (Z_1, Z_2)^T$, the correlated increments are $L \mathbf{Z}$.

For a detailed explanation see [this video on the Heston model](https://www.youtube.com/watch?v=HG3s2StHB3k).

## 3. Merton Jump Diffusion Model

The Merton model modifies the standard geometric Brownian motion by adding jumps:

\begin{equation*}
dS_t = (r - r_j) S_t dt + \sigma S_t dZ_t + J_t S_t dN_t
\end{equation*}

\begin{equation\*}
S\_= S\_{t-1} \left( e^{\left(r-r_j-\frac{\sigma^2}{2}\right)dt + \sigma \sqrt{dt} z_t^1}+
\left(e^{\mu_j+\delta z_t^2}-1 \right) y_t \right)
\end{equation\*}

\begin{equation*}
r_j = \lambda \left(e^{\mu_j+\frac{\delta^2}{2}}\right)-1
\end{equation*}

where $dN_t$ is a Poisson process representing jumps, and $J_t$ is the jump size. Simulation under this model involves generating asset paths with both continuous and jump components, and pricing options by averaging discounted payoffs.

## 4. Greeks Calculation

The Greeks measure sensitivities of option prices to various parameters. In this framework, Delta and Gamma are computed using finite difference methods:

- **Delta:** Sensitivity to underlying price.
- **Gamma:** Sensitivity of Delta to underlying price.

Finite difference approximations are used to estimate these derivatives numerically.

## 5. Barrier Options

Barrier options are path-dependent derivatives that only pay off if the underlying asset crosses a certain barrier. The framework includes methods for pricing up-and-in and down-and-in options under both the Heston and Merton models, using Monte Carlo simulation to determine whether the barrier is breached and to compute the discounted payoff accordingly.

## 6. Conclusion

This theoretical overview provides the mathematical and computational foundation for advanced option pricing models, including simulation, pricing, and risk analysis. The methods described here are applicable to a wide range of financial derivatives and serve as a reference for both theory and practical implementation.

[Read more →](https://github.com/SboneloMdluli/Financial-Engineering-Forum-Posts/blob/master/stochastic_pricing.ipynb)
