# Use Cases

## Anomaly Detection

Companies like Netflix and Amazon use autoencoders to detect anomalies in system logs and network traffic — the model learns "normal" patterns, and anything that reconstructs poorly is flagged as an anomaly. In cybersecurity, autoencoders detect intrusion attempts and fraud by flagging deviations from learned normal behavior.

## Healthcare & Medical Imaging
VAEs are used in medical imaging analysis — your own lab highlights this. In practice, hospitals and research labs use them to:
1. Denoise MRI and CT scans (reconstruct clean images from noisy ones)
2. Detect tumors and abnormalities (anomalies that don't reconstruct well)
3. Generate synthetic patient data for training when real data is scarce (privacy-preserving)
