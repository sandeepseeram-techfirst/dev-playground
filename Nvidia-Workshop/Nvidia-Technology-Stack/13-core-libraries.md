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