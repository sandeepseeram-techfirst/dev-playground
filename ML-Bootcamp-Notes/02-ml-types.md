## Types of Machine Learning Systems

There are three main types of machine learning systems: supervised, unsupervised, and reinforcement learning, plus a few useful variations.

### 1. Supervised learning (learning with labels)

- You train on input features plus correct outputs (labels), so the model learns a mapping from inputs to outputs.
- Two main problem types:
    - **Classification:** predict a discrete class (spam vs not spam, malignant vs benign, cat vs dog vs bird).
    - **Regression:** predict a continuous number (house price, temperature, expected number of customers).

**Flow / architecture diagram (text):**

- [Labeled Training Data (features + labels)] → [Supervised Learning Algorithm] → [Trained Model] → used on [New Input Features] → [Predicted Label or Value].

**Typical use cases:**

- Email spam detection, image labeling, medical diagnosis, price prediction, demand forecasting.

### 2. Unsupervised learning (finding structure in unlabeled data)

- You only have inputs, no labels; the system discovers patterns or structure on its own.
- Common tasks:
    - **Clustering:** group similar data points (e.g., customer segments, news article groups).
    - **Dimensionality reduction:** compress high‑dimensional data into fewer dimensions while keeping important information (for visualization or as preprocessing).
    - **Association rule learning:** find “items that go together” (e.g., customers who buy diapers often also buy beer).

**Flow / architecture diagram (text):**

- [Unlabeled Data] → [Unsupervised Learning Algorithm] → [Clusters / Lower‑Dim Representation / Association Rules].

**Typical use cases:**

- Market segmentation, topic grouping, anomaly detection, data compression and visualization, shopping basket analysis.

### 3. Reinforcement learning (learning by trial and error)

- An **agent** interacts with an **environment**, observes a **state**, takes an **action**, and receives a **reward or penalty**.
- Over time, the agent learns a **policy**: a strategy for choosing actions that maximizes long‑term cumulative reward.

**Key components:**

- Agent: learner/decision maker.
- Environment: world it interacts with.
- State: current situation.
- Action: choice agent makes.
- Reward/penalty: feedback signal.

**Interactive loop diagram (text):**

- [Agent observes State] → chooses [Action] → Environment → returns [New State, Reward/Penalty] → Agent updates Policy → repeat.

**Typical use cases:**

- Training robots, game‑playing AI (e.g., AlphaGo), traffic light control, long‑term personalized recommendation policies.

### 4. Other variations

- **Semi‑supervised learning:** small labeled dataset + large unlabeled dataset, useful when labels are expensive.
- **Self‑supervised learning:** create labels automatically from the data itself (e.g., predict the next word in a sentence); often treated as a form of unsupervised learning.

### Visual summary of all types

You can visualize the three main types side‑by‑side:

- Supervised: [Inputs + Labels] → learn f(x)→y*f*(*x*)→*y* → predict labels/values for new x*x*.
- Unsupervised: [Inputs only] → find structure (clusters, low‑dim space, rules) in x*x*.
- Reinforcement: [Agent ↔ Environment loop] → learn a policy π(s)*π*(*s*) that maximizes long‑term reward via trial and error.

This gives you a clean mental model of the **architectures** and **design patterns** behind most ML solutions you will encounter.