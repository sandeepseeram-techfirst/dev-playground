### Nvidia SMI 
SMI - Server Management Interface 
NVIDIA‑SMI is a single‑node GPU monitoring and basic management CLI tool that ships with the NVIDIA GPU driver and lets you quickly see and tweak GPU state on that host.

#### What NVIDIA‑SMI is and scope? 
Stands for NVIDIA System/Server Management Interface; it runs as the nvidia-smi command.
​Scope is one system/node only; it cannot pull data from remote nodes or aggregate a cluster.
​**Primary role:** quick GPU monitoring and basic management actions for GPUs on a single machine.

#### What NVIDIA‑SMI can manage
Beyond monitoring, it can perform basic control and configuration on that node:
​

Change GPU configuration settings, including some MIG‑related settings (where applicable).
​

Set power limits for GPUs (cap max power draw).
​

Change compute modes (e.g., default vs exclusive).
​

Terminate GPU processes if required (e.g., kill a misbehaving job).