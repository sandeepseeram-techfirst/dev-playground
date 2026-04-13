import torch

cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")

gpu_name = torch.cuda.get_device_name(0)
print(f"GPU: {gpu_name}")

total_vram_gb = torch.cuda.get_device_properties(0).total_mem / 1e9
print(f"VRAM: {total_vram_gb:.1f} GB")