---
title: "Lattice Pricing Models"
date: 2025-03-02
summary: "Implementation of binomial and trinomial lattice models for pricing options, including European, American, and Asian options with delta hedging strategies."
draft: false
featured: false
tags: ["Derivatives"]
categories: ["Derivatives"]
math: true
---

## Binomial Tree Model

We can price options in discrete time through lattice models. The first model we consider is the Cox-Ross-Rubinstein Model which is risk neutral under Martingale measure $\mathbb{Q}$. A process $S$ is a Martingale with respect to measure $\mathbb{Q}$ and filtration $\\{\\mathcal{F}_t\\}\_{t \geq 0}$, if $ \mathbb{E}^{\mathbb{Q}}[X_t \mid \mathcal{F}_s] = X_s \quad \forall \, s\leq t$. This means the process is path unbiased.

According to this model the stock at time $t$ can move to up by a factor of $u$ with probability $p$ and down by a factor of $d$ with probability $(1-p)$ at the next time step $t+1$. Using the principle of no arbitrage, the stock earns a risk free interest ($r$) and parameters $d < 1 < u$. The risk neutral probability $p$ is then given by mean matching.

\begin{equation}
\begin{aligned}
\begin{aligned}
\mathbb{E}[S_{t+\Delta t}] &= S_0e^{r\Delta t} \\\\
S_0e^{r\Delta t} &= S_0u\cdot p+S_0d\cdot(1-p) \\\\
\implies p &= \frac{e^{r\Delta t}-d}{u-d}
\end{aligned}
\end{aligned}
\end{equation}

Similarly the call option $c_0 = e^{-rT}(c_u\cdot p+c_d\cdot(1-p))$. We can evaluate $u$ and $d$ by matching the variance.

\begin{equation}
\begin{aligned}
\mathbb{V}(S*{t+\Delta t}) &= \mathbb{E}[(S*{t+\Delta t})^2] - (\mathbb{E}[S_{t+\Delta t}])^2 \\\\
\sigma^2 \Delta t &= p \cdot u^2 + d^2(1-p) + (p \cdot u^2 + d^2(1-p))^2 \\\\
\sigma^2 \Delta t &= (p -p^2)(u-d)^2 \\\\
\sigma^2 \Delta t &= e^{r\Delta t} (u+d) - u \cdot d - e^{2r\Delta t} \\\\
\sigma^2 \Delta t &= e^{r\Delta t} (u+1/u) - u \cdot 1/u - e^{2r\Delta t} \quad \text{[$u\cdot d=1$ ]} \\\\
u &= e^{\sigma \sqrt{\Delta t}} \\\\
d &= e^{-\sigma \sqrt{\Delta t}}
\end{aligned}
\end{equation}

The above definitions rely on a sufficiently small $\Delta t$ for $p$ to be a valid probability.

## Delta Hedging

We define a portfolio $\Pi_{t}$, under the principle of no arbitrage the portfolio is worth the same at time $t$ regardless of the path takes to $t+1$. Only the weights of the assets is allowed to change in the portfolio, no cash injection or deposits are allowed once the portfolio has been created, this is referred to as a self financing trading strategy.

\begin{equation}
\begin{aligned}
\Pi\_{t,u} &= \Delta S_0 u - c_u \quad \text{upward movement}
\end{aligned}
\end{equation}

\begin{equation}
\begin{aligned}
\Pi\_{t,d} &= \Delta S_0 d - c_d \quad \text{downward movement}
\end{aligned}
\end{equation}

Rebalancing under this constraints leads to delta hedging.

\begin{equation}
\begin{aligned}
\Delta S_0 d - c_d &= \Delta S_0 u - c_u \\\\
\Delta &= \frac{c_u-c_d}{S_0 u - S_0 d}
\end{aligned}
\end{equation}

$\Delta$ is the amount of the underlying that we must own for the portfolio to admit no arbitrage.

## American Binomial Tree

The American binomial tree extends the standard binomial model to handle early exercise options. At each node, we compare the immediate exercise value with the discounted expected future value to determine the optimal exercise strategy.

## Trinomial Tree

The trinomial tree model extends the binomial model by allowing for an additional middle state. This provides more flexibility in modeling the underlying price process and can lead to faster convergence compared to binomial trees.

## Asian Binomial Tree

The Asian binomial tree model is used for pricing Asian options where the payoff depends on the average price of the underlying asset over some time period. The model tracks the average price along each path and computes the option value accordingly.

[Read more →](https://github.com/SboneloMdluli/Financial-Engineering-Forum-Posts/blob/master/lattice_pricing_models.ipynb)
