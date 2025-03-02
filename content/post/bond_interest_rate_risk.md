---
title: "Understanding Bond Interest Rate Risk"
date: 2024-01-15
summary: "A bond is a fixed-income instrument consisting of periodic coupon payments and a face value, with its price determined by discounting these cash flows using the yield to maturity (YTM). The bond's price sensitivity to interest rate changes, known as volatility, is measured using duration and convexity, where higher duration indicates greater sensitivity to rate fluctuations."
draft: false
tags: ["Risk Management"]
categories: ["Risk Management"]
math: true
---

A bond is a fixed income instrument consisting of coupon payments and the face value (Fv). Coupons are regular payments, often expressed as a percentage of the face value. The price of a bond is calculated as the present value of its future cash flows, given by:


$$P =\sum_{i=1}^{n} \frac{C_i}{(1+r)^i} + \frac{Fv}{(1+r)^n}$$

Where $ C_i $ is the coupon value at time $t$, $n$ is the number of periods before maturity and $r$ is the yield to maturity. Yield to maturity is the expected return of the bond if held till maturity. Given a coupon rate $C_r$, if $ r \lt C_r $ then the bond is trading at a premium, if $ r \gt C_r $ the bond is issued at a discount and if $ r = C_r $ the bond is at par value. The equation above can be simplified to make computation easy.


$$P = \frac{C(1-(1+r)^{-n})}{r} + \frac{Fv}{(1+r)^n}$$

[Read more →](https://github.com/SboneloMdluli/Financial-Engineering-Forum-Posts/blob/master/bond_interest_rate_risk.ipynb)
