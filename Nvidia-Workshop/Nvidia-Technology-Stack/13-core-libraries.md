### Nvidia Core Libraries

#### CUDA: what it is (high level)
CUDA = Compute Unified Device Architecture.
​It is:
- A compute platform for GPUs.
- A unified device architecture so you can use GPUs for general computing, not just graphics.
​
CUDA has revolutionized GPU usage by making parallel programming on GPUs straightforward from languages like C/C++ and Python.


#### CUDA:

GPU can be used for:

* Graphics rendering (as before).
​
* Image and video processing (e.g., filters, transformations, encoding/decoding accelerations).
​
* Machine learning and AI workloads (training and inference, where many matrix operations run in parallel).
​
* Financial modeling and simulations (Monte Carlo, risk calculations, etc.).

CUDA is called a programming model because it defines how you structure and think about parallel code for GPUs.

#### How CUDA executes your code conceptually? 

* You write your logic in C/C++/Python or higher-level libraries.
​
* CUDA breaks the problem into many small, similar tasks that can be done in parallel.
​
* It launches thousands of threads (workers) on the GPU to perform those tasks simultaneously.
​
* When all threads finish, CUDA collects and aggregates the results so your program can continue.

#### Key Summary 

* CUDA is NVIDIA-only, tightly coupled to NVIDIA GPUs and drivers.
* It is a parallel computing platform + API + programming model to run general-purpose compute on GPUs.
​* Most AI developers use it indirectly through frameworks like TensorFlow, PyTorch, NCCL, and RAPIDS, which sit on top of CUDA.
​* Typical use cases include AI/ML training and inference, data analytics, simulations, and any workload with many similar operations that benefit from parallel execution.

#### CUDA Installation 
CUDA installation is mainly about meeting basic requirements, installing the CUDA Toolkit, and using nvidia-smi to verify the version and GPU details.

[Hardware]  -->  NVIDIA GPU (supported model)
[OS]        -->  Supported Linux / Windows
[Tools]     -->  GCC compiler (on Linux)
                        +
                CUDA Toolkit installer

1. Check GPU + OS support
2. Ensure prerequisites (e.g., GCC)
3. Download CUDA Toolkit from NVIDIA
4. Run installer (per NVIDIA docs)
5. Verify installation with nvidia-smi

#### Verifying CUDA installation with nvidia-smi
Use the nvidia-smi command to check the installed CUDA version and GPU status.

**​nvidia-smi shows:**

* CUDA version installed (e.g., “CUDA Version 13”).
​* Number of GPUs in the system.
​* Driver version and GPU details.
​* Memory capacity and current utilization.
​* Compute capability, GPU utilization, and power usage.

[nvidia-smi]
     |
     +--> Driver version
     +--> CUDA version
     +--> GPU count & names
     +--> Memory total / used
     +--> Utilization (%)
     +--> Power draw
