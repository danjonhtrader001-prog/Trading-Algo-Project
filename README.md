
## Project: Algorithmic Trading and Probability

### General introduction

This project gathers several **quantitative finance Python scripts** illustrating key concepts from **probability**, **statistics**, and **integration** applied to algorithmic trading: standard probability laws, the birthday paradox, entropy, concentration inequalities, stochastic dominance, Lebesgue integration applied to payoffs, and more.  
Each module provides either a **Monte Carlo simulation** or a **graphical visualization** (using `matplotlib`), and systematically highlights a **financial interpretation** (PnL, tail risks, diversification, capital allocation…).

### Overview of the modules

- **Birthday paradox** (`paradoxe_des anniversaires`): Monte Carlo simulation of the probability that two individuals in a group share the same birthday as the group size increases.
- **Standard discrete laws** (`loi_usuelles_discrètes`): simulation of **Bernoulli**, **binomial**, **Poisson**, and **geometric** laws, with interpretation in terms of trade sequences and order arrivals.
- **Standard continuous laws** (`loi_usuelles_densité`): illustration of classical continuous laws (normal, exponential, uniform, gamma, Student, Weibull, Laplace, Gumbel, Cauchy) to model returns, waiting times, and extreme risks.
- **Probabilistic entropy and diversification** (`entopie_probabiliste_diff`): computation of **Shannon entropy** to quantify market uncertainty and portfolio diversification.
- **Markov, Jensen, and Chebyshev inequalities** (`Markov_tcheb`): numerical illustration of concentration inequalities on a simulated PnL and returns, with visualizations.
- **Lebesgue vs Riemann integral** (`lebesgue`): comparison between Riemann and Lebesgue integrals (via Monte Carlo) for the expectation of an option‑like payoff `max(X-K, 0)`.
- **Stochastic dominance** (`domination_stochastique`): comparison of two normal distributions to illustrate **first‑order stochastic dominance** and its role in strategy choice.
- **Wigner semicircle law** (`Loi semi circulaire de wigner`): spectrum of random Wigner matrices and convergence to the semicircle law in random matrix theory.
- **Gaussian tail simulation** (`simulation_de _queue_Gauss`): simulation of a random variable truncated to the positive half of a Gaussian (tail).
- **Blackjack and Monte Carlo** (`black_jack`): simulation of many Blackjack hands to estimate the probabilities of win, loss, and push for a simple strategy.
- **Mean and variance on real data** (`application_var&Exp`): computation of **mean** and **variance** of daily returns for a stock (`AAPL`) from real market data (via `yfinance`).
- **Capital allocation and Bose–Einstein condensation** (`bose_einstein.py`): analogy between Bose–Einstein condensation and capital concentration on the most “attractive” companies.

---

### Birthday paradox

#### Mathematical intuition

The birthday paradox is based on **combinatorics**. For a group of \( n \) people, we compute the probability that at least two of them share the same birthday, assuming 365 possible days (non‑leap year) and **independent, equally likely** dates. We start from the complementary probability (no shared birthday), which is the product of decreasing terms, and then deduce the desired probability. As soon as the group reaches 23 people, this probability exceeds 50%, which is highly counterintuitive.

#### Link with algorithmic trading

This paradox shows how our intuition can fail in the presence of **rare but combinatorial events**, similar to **price coincidences**, **hash collisions**, or clusters of events on markets. It emphasizes the importance of reasoning in probabilities over large sets (orders, ticks, signals) rather than relying on naive intuition when assessing the likelihood of supposedly “improbable” scenarios.

#### Python implementation

The script `paradoxe_des anniversaires` performs a **Monte Carlo simulation**: for each group size from 1 to 60, it runs many trials (by default 1,000) drawing random birthdays. It estimates how often at least one coincidence occurs and plots the estimated probability as a function of group size, with a reference line at 50%.

---

### Standard discrete laws

#### Mathematical intuition

The **discrete** laws Bernoulli, binomial, Poisson, and geometric respectively model:  
- a single binary success/failure trial (Bernoulli);  
- the number of successes in a finite series of independent trials (binomial);  
- the number of events in a given time interval (Poisson);  
- the number of failures before the first success (geometric).  
They form the basis of many probabilistic models in finance and risk management.

#### Link with algorithmic trading

In algorithmic trading, these laws are used to model:  
- the outcome of a single trade (Bernoulli);  
- the distribution of the number of winning trades over a given period (binomial);  
- the random arrival of orders or “spikes” in the order book (Poisson);  
- the waiting time (in number of attempts) until a winning trade or a specific market event (geometric).  
They enable **backtesting** and **stress testing** of strategies by characterizing the variability of their results.

#### Python implementation

The script `loi_usuelles_discrètes` generates many samples from each law using `numpy.random` and displays comparative **histograms**. Comments document each law’s typical use in trading (win rate, order flow, waiting times, etc.), making the script a pedagogical bridge between discrete theory and market practice.

---

### Standard continuous laws

#### Mathematical intuition

Continuous laws such as the **normal**, **exponential**, **uniform**, **gamma**, **Student**, **Weibull**, **Laplace**, **Gumbel**, and **Cauchy** distributions provide a range of models for real‑valued variables: fluctuations around a mean, waiting times, accumulation phenomena, heavy tails, extreme values, or ultra‑erratic behavior (infinite variance).

#### Link with algorithmic trading

These laws are used to model **returns**, **inter‑trade durations**, **times to incidents** or crashes, and **extreme outcomes** (drawdowns, volatility spikes). In practice, using an inappropriate distribution (e.g., normal instead of Student or Cauchy) leads to underestimating tail risks, which is critical for **risk management** and strategy calibration.

#### Python implementation

The script `loi_usuelles_densité` simulates, for each law, a large number of samples and plots **normalized histograms** on a grid of subplots. Each subplot is annotated with the law’s financial role (standard returns, waiting times, accumulated risks, fat tails, extreme values, highly erratic markets, etc.).

---

### Probabilistic entropy and diversification

#### Mathematical intuition

**Shannon entropy** measures the level of **uncertainty** or **disorder** of a discrete probability distribution. It is minimal when the distribution is highly concentrated (one almost certain scenario) and maximal when all scenarios are equally likely. For a law \((p_i)_i\), entropy is defined as \(-\sum_i p_i \log_2 p_i\).

#### Link with algorithmic trading

In finance, entropy can quantify:  
- the uncertainty of **market scenarios** (up, flat, down);  
- the degree of **diversification** of a **portfolio**: a highly concentrated allocation has low entropy, whereas an equally‑weighted portfolio maximizes entropy.  
It is a conceptual tool connecting **information**, **diversification**, and **uncertainty**.

#### Python implementation

The script `entopie_probabiliste_diff` defines an entropy function, evaluates several distributions representing directional, uncertain, or intermediate markets, and then plots entropy values as bars. It also compares different portfolio allocations (all in one asset, two equal assets, diversified portfolios, concentrated portfolios), showing how entropy increases with diversification.

---

### Markov, Jensen, and Chebyshev inequalities

#### Mathematical intuition

The **Markov**, **Jensen**, and **Chebyshev** inequalities provide general bounds on the probabilities of extreme events and on expectations of convex functions.  
- Markov bounds \( \mathbb{P}(X \ge a) \) by \( \mathbb{E}[X]/a \) for \( X \ge 0 \).  
- Jensen compares \( f(\mathbb{E}[X]) \) to \( \mathbb{E}[f(X)] \) for a convex function \( f \).  
- Chebyshev bounds the probability of large deviations from the mean in terms of the variance.

#### Link with algorithmic trading

These inequalities help **bound tail risks** and “rare” events without knowing the exact distribution. For a log‑normal PnL or simulated returns, they provide simple upper bounds on the probabilities of extreme losses or gains and help reason about how **concentrated** a distribution is. They are useful in **risk management**, **conservative backtesting**, and communication of “worst‑case” style bounds.

#### Python implementation

The script `Markov_tcheb` simulates a log‑normal PnL and returns, computes empirical probabilities of certain events (PnL beyond a threshold, deviations from the mean), and compares them with Markov and Chebyshev bounds. It also illustrates Jensen using \( f(x) = e^x \). Several plots show the PnL distribution, the extreme region considered, and lines for the mean and multiples of the standard deviation.

---

### Lebesgue vs Riemann integral for an option payoff

#### Mathematical intuition

The **expectation** of a payoff \( f(X) \) can be viewed either as a **Riemann integral** (summing \( f(x)p(x)\,dx \) over the price axis) or as a **Lebesgue integral** (summing contributions from individual realizations of \( X \)). In probability theory, the Lebesgue integral is the natural framework for defining expectation.

#### Link with algorithmic trading

In option pricing, the expectation of the payoff \( \max(X-K, 0) \) under a given probability measure is central to **pricing** and **risk‑neutral valuation**. Understanding the equivalence between these two viewpoints (integral over the density vs Monte Carlo average) is key to justifying numerical pricing methods.

#### Python implementation

The script `lebesgue` simulates a Gaussian return, constructs the payoff `max(x-K, 0)`, and compares:  
- a **Riemann** approximation via a grid `x_grid` and the sum of \( f(x) p(x)\,dx \) (using `scipy.stats.norm`);  
- a **Lebesgue** approximation via the Monte Carlo mean `np.mean(payoff)`.  
Plots display the normal density, the weighted payoff area, and the sample contributions to the Lebesgue integral.

---

### Stochastic dominance

#### Mathematical intuition

A random variable \( Y \) **stochastically dominates** \( X \) (first order) if, for every \( x \), \( F_X(x) \ge F_Y(x) \). Intuitively, \( Y \) delivers more high values than \( X \) and is thus “better” in terms of risk‑return for any investor who prefers more to less.

#### Link with algorithmic trading

When comparing strategies or portfolios, stochastic dominance allows us to compare PnL distributions: if one strategy dominates another, it is preferred by any **risk‑averse** investor with a standard utility. It is an important theoretical tool for **strategy ranking** and decision theory.

#### Python implementation

The script `domination_stochastique` simulates two normal laws \( X \sim \mathcal{N}(0,1) \) and \( Y \sim \mathcal{N}(1,1) \), computes their **empirical distribution functions**, and plots them on the same axes. It also shows empirical densities to highlight the rightward shift of \( Y \), numerically illustrating stochastic dominance.

---

### Wigner semicircle law

#### Mathematical intuition

In **random matrix theory**, the spectrum (set of eigenvalues) of large symmetric matrices with Gaussian entries, once normalized, converges to the **Wigner semicircle law**. Its density is supported on a compact interval and has a half‑circle shape.

#### Link with algorithmic trading

Random matrices arise in **portfolio risk management** (correlation/covariance matrices of many assets). Understanding the typical spectrum of such matrices helps separate **random noise** from **structural factors** (significant extreme eigenvalues), which is crucial for dimensionality reduction and managing multi‑asset portfolios.

#### Python implementation

The script `Loi semi circulaire de wigner` generates a Wigner matrix (symmetric with Gaussian entries), computes its eigenvalues, normalizes them, and plots the empirical histogram together with the theoretical semicircle density. It illustrates the convergence of the spectrum to this law as the matrix dimension grows.

---

### Gaussian tail simulation

#### Mathematical intuition

A **Gaussian tail** is the truncated part of a normal distribution, e.g. \( X \sim \mathcal{N}(0,1) \) conditioned on \( X > 0 \). It models phenomena that can only take positive values but inherit a Gaussian‑like shape over their support.

#### Link with algorithmic trading

Such variables can model **magnitudes** of positive moves, strictly positive times, or other quantities naturally bounded below by zero. Visualizing the Gaussian tail helps understand how **truncation** alters the distribution and thus risk evaluation.

#### Python implementation

The script `simulation_de _queue_Gauss` simulates a standard Gaussian, filters strictly positive values, and plots the normalized histogram of the right half, highlighting the shape of the tail.

---

### Blackjack and Monte Carlo simulation

#### Mathematical intuition

Blackjack is a **probabilistic** game where the player faces the dealer under simple drawing rules. Its structure naturally lends itself to **Monte Carlo simulation** to estimate probabilities of winning, losing, or pushing under various strategies.

#### Link with algorithmic trading

Modeling this game is a good sandbox for testing ideas about **risk management**, **decision rules** (hit or stand), and illustrating how simple rules generate complex outcome distributions. It provides intuition close to **trading systems** (position sizing, stop‑loss rules, mechanical strategies).

#### Python implementation

The script `black_jack` defines a hand representation, a simple strategy for both player and dealer, and then runs many hands (by default 100,000). It returns the observed frequencies of wins, losses, and pushes for the player, giving an empirical estimate of the house edge for this naive strategy.

---

### Mean and variance on real data

#### Mathematical intuition

**Mean** and **variance** are, respectively, the average and the dispersion measure of a series of returns. On real market data, their estimation quantifies an asset’s **average gain** and **risk**.

#### Link with algorithmic trading

These quantities underpin **portfolio management** (risk/return ratio, volatility), **indicator construction**, and model calibration (e.g., constant variance vs stochastic volatility). They are also the starting point for risk‑adjusted performance measures.

#### Python implementation

The script `application_var&Exp` downloads daily prices for the `AAPL` stock via `yfinance`, computes **daily returns**, and then their mean and variance using `numpy`. Results are displayed in percentage terms for direct interpretation.

---

### Capital allocation and Bose–Einstein condensation

#### Mathematical intuition

The **Bose–Einstein** distribution describes the allocation of indistinguishable particles over energy levels, with possible **condensation** on the ground state. By analogy, a given amount of capital can concentrate on a few highly attractive companies.

#### Link with algorithmic trading

This module shows how “increasing attractiveness” mechanisms can lead to **strong capital concentration** in a handful of names (superstar effect). It offers a useful analogy for thinking about sector concentration, asset bubbles, and systemic fragility.

#### Python implementation

The script `bose_einstein.py` defines a set of companies with increasing **attractiveness**, computes a Bose–Einstein‑type population over their energy levels, then normalizes it to a given total capital. It plots a bar chart showing the capital share allocated to each company.

---

### How to run the scripts

#### Prerequisites

- **Python 3.x**
- Python libraries: `numpy`, `matplotlib`, `yfinance`, `scipy` (for some modules)

#### Installing dependencies

From the project directory:

```bash
pip install numpy matplotlib yfinance scipy
```

#### Example commands

Each module can be launched from the terminal by calling Python on the corresponding file:

```bash
# Birthday paradox
python "paradoxe_des anniversaires"

# Standard discrete laws
python "loi_usuelles_discrètes"

# Standard continuous laws
python "loi_usuelles_densité"

# Entropy and diversification
python entopie_probabiliste_diff

# Markov / Jensen / Chebyshev inequalities
python Markov_tcheb

# Lebesgue vs Riemann integrals
python lebesgue

# Stochastic dominance
python domination_stochastique

# Wigner semicircle law
python "Loi semi circulaire de wigner"

# Gaussian tail simulation
python "simulation_de _queue_Gauss"

# Blackjack
python black_jack

# Mean and variance on real data
python application_var&Exp

# Bose–Einstein‑type allocation
python bose_einstein.py
```

Depending on your environment, you may need to add the `.py` extension for some files or adjust commands slightly if you rename scripts.
