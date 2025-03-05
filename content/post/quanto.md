---
title: "Quanto Options"
date: 2025-03-02
summary: "Quanto options are derivatives that protect foreign investors from currency risk by fixing the exchange rate for payoffs, with valuation models differing between domestic and foreign perspectives."
draft: false
featured: false
tags: ["Derivatives"]
categories: ["Derivatives"]
math: true
---

As a foreign investor buying assets in a foreign market you are exposed to currency rate risk. A Quanto is a derivative whose payoff is written In a foreign currency denomination. The payoff is converted at a predetermined exchange rate allowing the foreign investor to hedge against currency rate risk. The valuation differ on perspective,

Valuation differs based on perspective:

Valuation from domestic investor perspective:
$
dS^d_t = S^d_t (\mu^d dt + \sigma^d_s dW^d_t)
$

Valuation from foreign investor perspective in their domestic denomination:
$
dS^f_t = S^f_t \left( r^f - \rho \sigma^d_s \sigma^f_x \right) dt + S^f_t \left( \sigma^f_x d\tilde{W}^f_t \right)
$

using Girsanov theorem $W^f_t$ under change of measure is,

$
\tilde{W}^f_t = W^f_t + \frac{\rho \sigma^d_s d t + \mu^d - r^f}{\sigma^d_s}
$

This is a Brownian motion accounting for market risk adjusted for exchange rate, enabling the valuation of the derivative in the foreign investor's domestic currency.

- $ r^f $ is the risk-free rate in foreign currency,
- $ \rho $ is the correlation between foreign exchange (FX) and stock,
- $ \sigma^d_s $ is the stock volatility,
- $ \sigma^f_x $ is the FX rate volatility.
