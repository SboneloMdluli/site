---
title: "Stochastic Pricing Models"
date: 2025-05-10
summary: "This article provides an exposition of stochastic models for option pricing, focusing on the mathematical formulation and computational techniques underlying the Heston and Merton jump-diffusion frameworks. Analytical and simulation-based approaches for pricing, risk management, and sensitivity analysis are discussed in detail."
tags: ["Quantitative Finance", "Derivatives"]
categories: ["Quantitative Finance"]
math: true
---

# Stochastic Pricing Models

This post presents the theoretical foundations of stochastic models for option pricing. We outline the mathematical structure and computational methods for European and American options under both the Heston and Merton jump-diffusion models, including the calculation of Greeks and barrier options.

## 1. Introduction to Stochastic Option Pricing

Stochastic models are essential for capturing the randomness in financial markets, especially for pricing derivatives like options. Two widely used models are:

- **Heston Model**: Incorporates stochastic volatility, allowing volatility to evolve randomly over time.
- **Merton Jump Diffusion Model**: Extends the Black-Scholes framework by adding random jumps in asset prices, capturing sudden market moves.

## 2. Heston Model

The Heston model jointly evolves the asset price $S_t$ and its instantaneous variance $v_t$ (so volatility is $\sqrt{v_t}$):

\begin{equation*}
dS_t = \mu S_t dt + \sqrt{v_t}\ S_t\ dW_t^S
\end{equation*}

\begin{equation*}
dv_t = \kappa (\theta - v_t) dt + \sigma \sqrt{v_t}\ dW_t^v
\end{equation*}

Here, $\mu$ is the drift term, $\kappa$ is the speed of mean reversion of variance, $\theta$ is the long-run variance level, and $\sigma$ is the volatility of variance (vol-of-vol). The shocks $dW_t^S$ and $dW_t^v$ are Brownian increments for the price and variance processes, respectively, and they satisfy:

\begin{equation*}
dW_t^S dW_t^v = \rho dt
\end{equation*}

Simulation of the Heston model involves generating correlated random walks for price and variance, and pricing options via Monte Carlo and Least Squares Monte Carlo (LSMC) methods. LSMC is used for American options, regressing future payoffs to estimate optimal early exercise.

To simulate correlated shocks, let $Z_1$ and $Z_2$ be independent standard normals and set:

Let $Z_1$ and $Z_2$ be independent standard normal random variables. The correlated Brownian increments can be constructed as:

\begin{equation*}
dW_t^S = \sqrt{dt}\ Z_1
\end{equation*}

\begin{equation*}
dW_t^v = \rho \sqrt{dt}\ Z_1 + \sqrt{1-\rho^2}\ \sqrt{dt}\ Z_2
\end{equation*}

This guarantees the required instantaneous correlation $\rho$. In matrix form, the correlation matrix is

$$
\Sigma = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}
$$

with Cholesky factor

$$
L = \begin{pmatrix} 1 & 0 \\ \rho & \sqrt{1-\rho^2} \end{pmatrix}
$$

so that, for $\mathbf{Z}=(Z_1,Z_2)^T$, the correlated increments are $L\mathbf{Z}$.

For a detailed explanation see [this video on the Heston model](https://www.youtube.com/watch?v=HG3s2StHB3k).

## 3. Merton Jump Diffusion Model

The Merton model extends geometric Brownian motion by adding a jump component:

\begin{equation*}
dS_t = (r - r_j) S_t dt + \sigma S_t dZ_t + J_t S_t dN_t
\end{equation*}

In this model, $r$ is the risk-free rate, $dZ_t$ is the diffusion shock, and $\sigma$ is diffusion volatility (distinct from the Heston vol-of-vol parameter). The Poisson increment $dN_t$ captures random jump arrivals, and $J_t$ controls jump size. The compensator $r_j$ adjusts drift so jump risk is accounted for in expectation.

\begin{equation*}
S_t = S_{t-1} \left( e^{\left(r-r_j-\frac{\sigma^2}{2}\right)dt + \sigma \sqrt{dt} z_t^1}+
\left(e^{\mu_j+\delta z_t^2}-1 \right) y_t \right)
\end{equation*}

\begin{equation*}
r_j = \lambda \left(e^{\mu_j+\frac{\delta^2}{2}}\right)-1
\end{equation*}

In the discrete update, $S_{t-1}$ is the previous-step price, $z_t^1$ drives the diffusion term, and the jump term uses a random jump indicator/count $y_t$ together with jump-size shock $z_t^2$. Parameters $\lambda$, $\mu_j$, and $\delta$ denote jump intensity, mean log-jump size, and log-jump volatility, respectively. Simulation proceeds by combining diffusion and jump parts pathwise, then discounting payoffs.

## 4. Greeks Calculation

The Greeks measure sensitivities of option prices to various parameters. In this framework, Delta and Gamma are computed using finite difference methods:

- **Delta:** Sensitivity to underlying price.
- **Gamma:** Sensitivity of Delta to underlying price.

Finite difference approximations are used to estimate these derivatives numerically.

## 5. Barrier Options

Barrier options are path-dependent derivatives whose payoff depends on whether the underlying touches a preset barrier during the option life. In a **knock-in** contract, the option becomes active only if the barrier is hit (for example, an up-and-in call activates only after the price rises to the barrier), while in a **knock-out** contract, hitting the barrier cancels the option (for example, an up-and-out call is extinguished once the barrier is reached). This makes barrier options generally cheaper than plain vanilla options with similar strikes, since activation/cancellation conditions reduce expected payoff in many paths. Under both Heston and Merton dynamics, pricing is performed by simulating full paths, checking barrier events at each time step, and then discounting the payoff only on paths that satisfy the specific knock-in or knock-out rule.

## 6. Conclusion

This theoretical overview provides the mathematical and computational foundation for advanced option pricing models, including simulation, pricing, and risk analysis. The methods described here are applicable to a wide range of financial derivatives and serve as a reference for both theory and practical implementation.

[Read more →](https://github.com/SboneloMdluli/Financial-Engineering-Forum-Posts/blob/master/stochastic_pricing.ipynb)
