---
title: "Put-Call Parity"
date: 2024-02-08
summary: "The put-call parity establishes the relationship between European call and put options with the same strike price and expiration date, demonstrating how a portfolio of options and the underlying asset can replicate a risk-free bond."
draft: false
tags: ["Derivatives"]
categories: ["Derivatives"]
math: true
---

The put-call parity (PCP) establishes the relationship between call and put options that share the same underlying asset and expiration date. This relationship is especially relevant for European options. To illustrate it, we can create a portfolio composed of a long put option ($P(t)=max(K-S_{t},0)$), a short call option ($C(t)=max(S_{t}-K,0)$), and a long position in a non-dividend-paying stock ($S$) of the underlying. Both options have the same strike price ($K$) and expiration date ($T$). The portfolio's structure before the expiration, at $t \leq T$, is described as follows:


\begin{equation}
\begin{split}
\prod_{t}^{} &= S_{t} + max(K-S_{t},0) - max(S_{t}-K,0)\\
&= K e^{-r(t-T)}
\end{split}
\end{equation}


for European options this portfolio is simply a bond with interest rate $r$ and maturity $T$, the portfolio then becomes $\prod_{T} = K$

[Read more →](https://github.com/SboneloMdluli/Financial-Engineering-Forum-Posts/blob/master/put_call_parity.ipynb)
