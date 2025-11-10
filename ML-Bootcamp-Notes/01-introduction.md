### Machine Learning

At its core, machine learning is about creating systems that can learn from data. Instead of programmers writing explicit, step-by-step instructions for every possible scenario, a machine learning system identifies patterns in data and builds its own logic based on those patterns.

Tom Mitchell (1997):

- A program learns from experience E*E* on tasks T*T* with performance measure P*P* if its performance at tasks in T*T*, measured by P*P*, improves as it gets more experience E*E*.

Breakdown of T,E,P.

- **Task (T):** What the system does. Examples:
    - Classify emails as spam/ham.
    - Predict house prices from size, location, etc.
    - Recognize handwritten digits.
- **Experience (E):** Data used for learning. Examples:
    - Labeled emails for spam filtering.
    - Historical house sales with features and prices.
- **Performance (P):** How success is measured. Examples:
    - Percentage of emails correctly classified.
    - Average error between predicted and actual house prices.

Goal: as we feed more and better data (experience), performance on the task improves according to the performance measure.