---
title: "Quanto Derivatives"
date: 2025-03-02
summary: "Quanto options are derivatives that protect foreign investors from currency risk by fixing the exchange rate for payoffs, with valuation models differing between domestic and foreign perspectives."
draft: false
featured: false
tags: ["Derivatives"]
categories: ["Derivatives"]
math: true
---

As a foreign investor buying assets in a foreign market you are exposed to currency rate risk. A Quanto is a derivative whose payoff is written In a foreign currency denomination. The payoff is converted at a predetermined exchange rate allowing the foreign investor to hedge against currency rate risk. The valuation differ on perspective,

Valuation from domestic investor perspective under domestic measure:

$dS^d_t = S^d_t (\mu^d dt + \sigma_s dW^d_t)$

Valuation from foreign investor perspective in their domestic denomination:
$
dS^f_t = S^f_t \left( r^f - \rho \sigma_s \sigma_x \right) dt + S^f_t \left( \sigma_s d\tilde{W}^f_t \right)
$

using Girsanov theorem to change measures, $\tilde{dW}^f_t$ is,

$
\tilde{dW}^f_t = \frac{\rho \sigma_s \sigma_x + \mu^d - r^f}{\sigma_s} + dW^f_t
$

This is a Brownian motion accounting for market risk adjusted for exchange rate, enabling the valuation of the derivative in the foreign investor's domestic currency.

- $ r^f $ is the risk-free rate in foreign currency,
- $ \rho $ is the correlation between foreign exchange (FX) and stock,
- $ \sigma^d_s $ is the stock volatility,
- $ \sigma^f_x $ is the FX rate volatility.
