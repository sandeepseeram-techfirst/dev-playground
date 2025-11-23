### Temperature

#### 1. What are `temperature` and `top_p`?

- Both control **how different** the model’s answers are each time.
- `temperature` (0.0–2.0, usually 0–1):
    - `0.0` → almost same answer every time (good for tests).
    - Higher → more creative / random.

- `top_p` (0.0–1.0):
    - Limits choices to the **top p% of likely tokens**.
    - Lower → safer, more focused; higher → more variety.

Use **one** of them (usually `temperature`), not both.

`javavar options = OpenAiChatOptions.builder()
    .withModel("gpt-4o")
    .withTemperature(1.0f)
    .build();`

---

#### 2. How do we measure “how different” responses are?

- **n‑grams** = chunks of `n` words in order (e.g., 2‑grams, 3‑grams).
- **Jaccard similarity** between two sets of n‑grams:

similarity=∣A∩B∣∣A∪B∣

similarity=∣

*A*

∪

*B*

∣∣

*A*

∩

*B*

∣

- `1.0` → texts basically the same.
- `0.0` → texts share nothing.

---

#### 3. Jaccard similarity service (core idea)

Service does:

1. Split text into words.
2. Build all n‑grams.
3. Make 2 sets (text1, text2).
4. Return intersection/union.

---

#### 4. Basic tests for the Jaccard service

They test 3 cases:

1. **Same text vs same text** → similarity ≈ `1.0`.
2. **Completely different sentences** → similarity ≈ `0.0`.
3. **One word changed** → similarity ≈ `0.7`.

This proves the metric behaves as expected.

---

#### 5. Variability tests for `temperature` and `top_p`

For each parameter (`temperature` or `top_p`):

1. Fix a prompt:
    
    > **“Write a story about a salamander learning to fly.”**
    > 
2. For multiple values (e.g., temperature from 0.0 → 2.0):
    - Call the model several times.
    - Compare each answer to the **first** using Jaccard similarity.
3. Use **linear regression** (`SimpleRegression`) on:
    - x = run index,
    - y = similarity.
4. Check the **slope**:
    - For `temperature`: slope should be **negative** (answers get more different).
    - For `top_p`: slope should be **non‑positive or very small** (< 0.05).

There’s also a tiny text “bar graph” with `*` characters in the logs to show similarity visually, but that’s just for nicer logging.

---

#### One-sentence recap

- `temperature` / `top_p` = knobs for randomness,
- Jaccard + n‑grams = way to **measure** how much answers change,
- Regression on those similarities = check that the knobs behave as expected.