### Kernel-level Programming

Kernel-level programming means writing code that runs at a very low level, close to the hardware or core execution engine (OS kernel or GPU/TPU device), to control how work and data move, rather than just calling high‑level APIs.

 We need it when generic libraries can’t give us enough performance, control, or custom behavior, and it works by executing special “kernel” functions across many threads with privileged or hardware-near access.

### In practice, “kernel-level programming” is used in two related but different contexts:

**OS kernel programming:** Writing code inside the operating system kernel (e.g., Linux kernel modules, device drivers) with full control over memory, scheduling, filesystems, networking, etc.

**GPU/TPU kernel programming:** Writing custom device kernels (CUDA, Triton, Pallas, etc.) that run massively parallel on accelerators to implement operations like matmul, attention, convolutions.

### OS kernel programming
The OS kernel is the core part of the operating system that manages hardware, memory, processes, filesystems, and networking.

**Kernel programming here means writing code (often as loadable kernel modules) that runs with high privilege, directly interacting with kernel subsystems to implement drivers, security modules, or system services.**

### GPU/TPU kernel programming
In GPU programming, a kernel is a function written to run on the GPU device and executed by many threads in parallel over large arrays of data.

A host program (CPU code) launches kernels with a grid configuration; each kernel instance (thread or thread block) processes a slice of the data, all running the same code on different indices.

**Frameworks like CUDA, Triton, and Pallas let you express how data is partitioned into tiles and how threads cooperate to load, compute, and store results efficiently.**