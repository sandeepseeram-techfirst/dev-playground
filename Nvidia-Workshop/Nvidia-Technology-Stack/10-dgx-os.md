### DGX OS 

#### DGX Operating System (DGX OS)
- NVIDIA provides a customized Ubuntu Long Term Support OS specifically for DGX systems.
​It is based on Ubuntu 22.04 LTS, with additional tuning and NVIDIA integration.
​This OS is called **DGX OS.**

* Generic OSes (Windows, generic Linux, generic hypervisors) are not optimized for DGX’s heavy AI/ML workloads.
* It ensures the hardware (GPUs, NICs, storage) and software stack all work together smoothly with the right versions and settings.

#### DGX OS has an NVIDIA‑optimized kernel tuned for:

* AI/ML
* Analytics
* High GPU utilization on DGX hardware.

#### DGX OS 
DGX OS is not just a bare Linux kernel; it includes a comprehensive software stack.
​
**Key components:**

* GPU driver (NVIDIA driver, matched to the hardware).
​* CUDA toolkit for GPU programming and acceleration.
​* cuDNN, NCCL, CUDA‑X‑type libraries (for deep learning, communications, etc.).
​* Docker engine: container runtime so you can run AI workloads as containers out of the box.
​
Other commonly used components that make the system ready for AI/ML and analytics use.

**Generic Ubuntu server:**
  - Install NVIDIA driver manually
  - Install CUDA manually
  - Install cuDNN, NCCL manually
  - Install Docker manually
  - Manually tune kernel & networking

**DGX OS:** 
  - Comes with all of the above pre-installed,
    version-aligned, and tuned for DGX AI workloads.
