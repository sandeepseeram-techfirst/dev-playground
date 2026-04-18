### Kernel-level Programming

Kernel-level programming means writing code that runs at a very low level, close to the hardware or core execution engine (OS kernel or GPU/TPU device), to control how work and data move, rather than just calling high‑level APIs.

 We need it when generic libraries can’t give us enough performance, control, or custom behavior, and it works by executing special “kernel” functions across many threads with privileged or hardware-near access.