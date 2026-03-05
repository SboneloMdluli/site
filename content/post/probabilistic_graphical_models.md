---
title: "Probabilistic Graphical Models"
date: 2026-02-22
summary: "A concise, formal overview of probabilistic graphical models (PGMs), including Bayesian networks, Markov networks, parameter and structure learning, and Markov blankets."
draft: false
tags: ["Machine Learning"]
categories: ["Machine Learning"]
math: true
---

Probabilistic graphical models (PGMs) provide a mathematical framework that combines probability theory and graph theory in order to represent complex relationships among random variables. Two broad classes of PGMs are commonly distinguished: belief networks (Bayesian networks) and Markov networks (Markov random fields).

## Preliminaries: probability and graphs

A probability space is defined by the triplet $\left(\Omega, \mathcal{F}, \mathbb{P}\right)$, where $\Omega$ is the sample space (the set of all possible outcomes of an experiment), $\mathcal{F}$ is a $\sigma$-algebra of events (subsets of $\Omega$), and $\mathbb{P}$ is a probability measure assigning a probability to each event in $\mathcal{F}$. 

Informally, a random variable $X$ is a measurable function $X: \Omega \to \mathbb{R}$, mapping outcomes in $\Omega$ to real numbers.

A fundamental identity in PGMs is the chain rule. Given random variables $X_1, \dots, X_n$, their joint distribution factorizes as:

$$
P(X_1, \ldots, X_n) = \prod_{i=1}^{n} P\left(X_i \mid X_1, \ldots, X_{i-1}\right)
$$

A graph $G$ is defined by a set of vertices $V$ and a set of edges $E$. There are two main types of graphs: directed and undirected.

- Directed graphs have edges with orientation, denoted as $X \rightarrow Y$, indicating that $X$ is a parent of $Y$.
- Undirected graphs have edges without orientation, so connections are symmetric between nodes.

In undirected graphs, the notion of a clique is important.

Definition (clique): A clique is a complete subgraph; that is, a set of vertices $C \subseteq V$ such that every pair of vertices in $C$ is connected by an edge. A clique is maximal if it is not properly contained in any larger clique.

## Belief networks (Bayesian networks)

A belief network is a directed acyclic graph (DAG) that represents conditional dependencies among random variables. The defining property is a local Markov condition: each variable is conditionally independent of its non-descendants given its parents. Consequently, the joint distribution factorizes as

$$
P(X_1,\ldots,X_n) = \prod_{i=1}^{n} P\\left(X_i \mid {\mathrm{Pa}(X_{i-1})}\right)
$$

where $\mathrm{Pa}(X_{i-1})$ denotes the set of parent nodes of $X_{i-1}$ in the DAG.

### D-separation

To formally describe conditional independence relationships among random variables in a belief network, one introduces directed separation (d-separation). The three canonical motifs are:

- Chain $(X \rightarrow Z \rightarrow Y)$

  $$
  P(x,z,y) = P(x)\ P(z\mid x)\ P(y\mid z)
  $$

- Fork $(X \leftarrow Z \rightarrow Y)$

  $$
  P(x,z,y) = P(z)\ P(x\mid z)\ P(y\mid z)
  $$

- Collider $(X \rightarrow Z \leftarrow Y)$ with $X \perp Y \mid Z$

  $$
  P(x,z,y) = P(x)\ P(y)\ P(z\mid x,y)
  $$

These motifs determine when paths transmit or block statistical dependence under conditioning, and they provide a graphical criterion for reading off conditional independences implied by the model.

Belief networks provide an efficient and interpretable representation of complex joint distributions through conditional independence. However, they may incur substantial computational cost and can scale poorly for large or densely connected systems. Moreover, the acyclicity constraint restricts the class of interactions that can be represented directly, which motivates the consideration of alternative undirected models.

## Markov networks (Markov random fields)

A Markov network is a probabilistic model represented by an undirected graph. In contrast to belief networks, the joint distribution is expressed in terms of nonnegative potential functions defined over cliques. Let $\mathcal{C}$ denote a collection of maximal cliques. The joint distribution takes the form

$$
P(x) = \frac{1}{Z}\prod_{C \in \mathcal{C}} \psi_C(x_C)
$$

where $\psi_C(x_C) \geq 0$ is a nonnegative potential function defined on the variables in clique $C$, and $Z$ is called the partition function. The partition function serves to normalize the distribution, ensuring that the total probability sums (or integrates) to 1.

### The partition function

The partition function $Z$ is defined so that $P(x)$ is a valid probability distribution. In the discrete case, where $x$ ranges over a finite or countable state space $\mathcal{X}$,

$$
Z = \sum_{x \in \mathcal{X}} \prod_{C \in \mathcal{C}} \psi_C(x_C)
$$

and in the continuous case the corresponding expression is an integral:

$$
Z = \int \prod_{C \in \mathcal{C}} \psi_C(x_C)\,dx
$$

Beyond its normalizing role, $Z$ (and its logarithm, the log-partition function) governs many quantities of interest, including marginal likelihoods and gradients used in parameter estimation for undirected models. In general, computing $Z$ exactly is intractable for large graphs, and practical methods rely on approximations

Markov networks satisfy the following Markov properties:

1. Global Markov property
2. Local Markov property
3. Pairwise Markov property

They represent conditional independence via graph separation and are more flexible than belief networks in that they impose no acyclicity constraint. Nonetheless, due to the absence of edge orientation, Markov networks do not directly encode causal relationships. A belief network can be transformed into an undirected graph via moralization, although such transformations do not, in general, preserve all conditional independence relations.

## Markov models (Markov chains)

Separately from Markov networks, the term Markov model is often used to refer to Markov chains, i.e., stochastic processes ${X_{t\ge 0}}$ that satisfy the Markov property. In discrete time, this property states that the conditional distribution of the next state depends only on the present state:

$$
\mathbb{P}(X_{t+1}=x \mid X_t, X_{t-1}, \ldots, X_0) = \mathbb{P}(X_{t+1}=x \mid X_t)
$$

Equivalently, $X_{t+1}$ is conditionally independent of $X_{t-1}, \ldots, X_0$ given $X_t$:


$$
X_{t+1} \perp (X_{t-1}, \ldots, X_0) \mid X_t
$$

For a finite-state, time-homogeneous discrete-time Markov chain, the dynamics are characterized by a transition matrix $ P $ with entries

$$
P_{ij} = \mathbb{P}(X_{t+1} = j \mid X_t = i),
$$

and the $k$-step transition probabilities are given by the entries of the matrix power $P^k$. Under standard conditions, the chain admits a stationary distribution $\pi$ satisfying

$$
\pi^\top P = \pi^\top.
$$

In continuous time, Markov chains are specified via an infinitesimal generator $ Q $, which encodes transition rates and yields transition probabilities via 

$$
P(t) = \exp(Qt).
$$

Common variants discussed in applications include discrete-time Markov chains (DTMCs), continuous-time Markov chains (CTMCs), absorbing chains, and reversible chains.

## Parameter learning and structure learning

It is important to distinguish between learning parameters and learning structure. These tasks play complementary roles in constructing and using graphical models.

### Parameter learning

Parameter learning concerns the estimation of numerical quantities (e.g conditional probabilities in a Bayesian network) when the graph structure is known or assumed. In discrete Bayesian networks, the parameters are commonly represented as conditional probability tables (CPTs), which quantify the distribution of each variable conditional on its parent configuration.

Two broad approaches are typical:

- Maximum likelihood estimation, which reduces to counting configurations and normalizing in the fully observed discrete case.
- Bayesian estimation, which combines prior beliefs with observed data (e.g using conjugate priors such as Dirichlet distributions for multinomial parameters).

When data are incomplete, parameter learning typically requires iterative procedures such as expectation–maximization (EM) or sampling-based methods (e.g Gibbs sampling).

### Structure learning

Structure learning aims to infer the graph topology from data, i.e., to determine which conditional dependencies should be represented by edges. This problem is substantially more difficult than parameter learning because the number of candidate structures grows rapidly with the number of variables.

Two major families of methods are:

- Constraint-based methods, which use statistical tests of conditional independence to prune edges and orient a compatible structure (e.g  PC algorithm).
- Score-based methods, which treat structure learning as an optimization problem by assigning scores that balance goodness-of-fit with complexity (e.g. BIC, BDe, MDL), then searching the space of structures via greedy or stochastic heuristics (e.g hill climbing, simulated annealing).

### Inferred causality algorithm (PC algorithm)

The PC algorithm is an example of this type of approach. It starts with a complete undirected graph that contains an edge linking every pair of variables, and gradually removes edges until the only edges remaining are directed edges oriented correctly.

Hybrid approaches combine these ideas, for example by learning an undirected skeleton via tests and then refining edge orientations using a scoring criterion. Practical challenges include computational complexity, the existence of Markov-equivalent structures, the need for increasing sample size as dimensionality grows, and the influence of latent variables.

### Key distinctions between parameter and structure learning

Parameter learning estimates numerical quantities associated with an assumed structure, whereas structure learning seeks to determine which conditional dependencies are present, often by identifying (in)dependencies among variables. In practice, parameter learning is typically computationally manageable under complete data, while structure learning is resource intensive and frequently relies on heuristic or approximate search procedures. Moreover, the sample complexity of structure learning increases rapidly with the number of variables, motivating constraints such as variable selection or limits on the maximum number of parents per node.

## Markov blankets

The Markov blanket of a target variable $X$ is the minimal set of variables that separates $X$ from the remainder of the graph, in the sense that conditioning on this set renders $X$ conditionally independent of all other variables.

In a Bayesian network, the (Pearl) Markov blanket of $X$ is:

- Parents of $X$
- Children of $X$
- Co-parents of $X$ (the other parents of $X$’s children)

If we write the Markov blanket as $\mathrm{MB}(X)$, the key property is:

$$
X \perp\!\!\!\perp \big( V \setminus (\{X\} \cup \mathrm{MB}(X)) \big) \;\big|\; \mathrm{MB}(X)
$$

The Markov blanket concept is frequently used for local prediction and inference: to predict $X$ it suffices, under the model assumptions, to condition on $\mathrm{MB}(X)$ rather than the full set of variables. Consequently, Markov blankets provide a principled criterion for identifying a compact set of variables that are most directly relevant to a target of interest.

### Types of Markov blankets

Two commonly cited notions are:

1. Pearl Markov blanket: the Bayesian-network construction described above (parents, children, and co-parents).
2. Friston Markov blanket: a boundary-state formalism used in active inference which partitions states into internal and external, mediated by sensory and active states.

### Advantages and limitations

Advantages of applying Markov blankets include:

1. Computational efficiency: inference and prediction for a target variable can be localized to a comparatively small subset of variables.
2. Interpretability: the blanket provides a compact description of the most directly relevant dependencies for a target.

Limitations include:

1. Discovery cost: in high-dimensional settings, identifying a minimal blanket (or a suitable approximation) can be computationally demanding.
2. Data requirements: reliable blanket identification may require substantial sample sizes. With limited data, estimated blankets may be unstable or misleading.

