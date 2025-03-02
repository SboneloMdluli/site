---
title: "Systematic Risk"
date: 2024-01-15
summary: "The article discusses systematic risk, which refers to the potential for widespread financial instability that cannot be mitigated through diversification but only through hedging. It highlights the importance of monitoring systematic risk for financial institutions and policymakers to manage risk exposure effectively."
draft: false
tags: ["Risk Management"]
categories: ["Risk Management"]
math: true
---

Key Concepts:

1. Value-at-Risk (VaR): A measure of the maximum potential loss over a period with a given confidence level. However, VaR has limitations, such as not considering tail dependency and lacking sub-additivity.
2. Expected Shortfall (ES): An improvement over VaR, ES is a coherent risk measure that calculates the average loss in scenarios where losses exceed VaR. It satisfies properties like monotonicity and sub-additivity.
3. Marginal Expected Shortfall (MES): Measures the contribution of a single institution to the overall systemic risk, calculated as the expected loss of an institution conditional on the system's loss exceeding VaR.
4. Capital Shortfall (CS): The amount by which an institution's capital falls short during a crisis. It is influenced by factors like leverage, size, and risk exposure.
5. Long Run Marginal Expected Shortfall (LRMES): An extension of MES over a longer horizon, estimating the expected loss of an institution during a market crash.

Value-At-Risk is the most a financial firm can loss over a period of time with some confidence $1-\alpha$. Formally VaR of $R$ is defined as follows:

$$\text{VaR}_{\alpha}(R) = -\inf\\{x:\mathbb{P}[R \leq x] \geq \alpha \\} = -\sup\\{x:\mathbb{P}[R \leq x] < \alpha \\}$$

[Read more →](https://github.com/SboneloMdluli/Financial-Engineering-Forum-Posts/blob/master/systematic_risk.ipynb)
