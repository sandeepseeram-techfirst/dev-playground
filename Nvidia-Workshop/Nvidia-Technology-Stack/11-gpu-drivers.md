### GPU Drivers 
A GPU driver is software that connects the NVIDIA GPU to the OS and to applications.
​Without the driver, the OS cannot properly use the GPU for compute or graphics workloads.

#### Preinstalled vs manual
* On preconfigured systems (DGX, some cloud images like AWS Deep Learning AMIs), the correct NVIDIA driver is often preinstalled.
​* On other machines, the driver may not be present and must be installed manually.

#### Lifecycle of using a GPU driver
1. Provision machine with NVIDIA GPU
2. Install or verify GPU driver:
   - If preconfigured image (DGX, DL AMI): driver likely already present
   - Else: follow NVIDIA docs for your OS
3. Run `nvidia-smi`:
   - Confirm driver version
   - Confirm GPU model & memory
   - Confirm CUDA version
4. Run applications/containers that use GPU
5. Use `nvidia-smi` again to see:
   - GPU utilization
   - Memory usage
   - Active GPU processes
