---
title: "How Limit Order Books Drive Price Discovery"
date: 2024-01-14
summary: "Explore how limit order books work and their role in market microstructure."
draft: false
featured: false
tags: ["Market Structure"]
categories: ["Market Structure"]
math: true
---

The Limit Order Book (LOB) is a fundamental mechanism in modern financial markets that facilitates price discovery and trading. This piece examines how LOBs work and their importance in market structure.

## Key Components

A limit order book contains:

- All active buy and sell orders
- Order volumes and prices
- Submission timestamps
- The current bid-ask spread

## Order Matching Protocols

Two main approaches are used:

1. Price-Time Priority (PTP)

- Orders sorted by price then time
- Rewards quick order submission
- Most common in equity markets

2. Pro Rata

- Orders at same price filled proportionally
- Encourages larger order sizes
- Common in some derivatives markets

The choice of protocol influences trader behavior and market efficiency.

## Definitions

**Bid Price**
The bid price at time t is the highest stated price among active buy orders at time t:

$$b(t) := \max_{x \in B(t)} \text{px}$$

**Ask Price**
The ask price at time t is the lowest stated price among active sell orders at time t:

$$a(t) := \min_{x \in A(t)} \text{px}$$

**Bid-Ask Spread**
The bid-ask spread at time t is:

$$s(t) := a(t) - b(t)$$

**Mid Price**
The mid price at time t is:

$$m(t) := \frac{a(t) + b(t)}{2}$$

[Read more →](https://github.com/SboneloMdluli/Financial-Engineering-Forum-Posts/blob/master/limit_order_book.ipynb)
