### DeepSeek-V4-Pro


DeepSeek-V4-Pro is a Mixture-of-Experts (MoE) language model with 1.6 trillion total parameters and 49 billion activated parameters. It features a hybrid attention architecture combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA), achieving 27% of single-token inference FLOPs compared to DeepSeek-V3.2 at 1M-token context. Post-training uses a two-stage pipeline: independent domain-expert cultivation (SFT + GRPO) followed by unified model consolidation via on-policy distillation.