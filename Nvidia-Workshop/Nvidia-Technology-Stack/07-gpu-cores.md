### GPU Cores 
CUDA cores, Tensor Cores, and RT (ray tracing) Cores. 

**CUDA cores**
* General‑purpose parallel compute and graphics rendering.
* ​Handle game graphics, simulations, physics, shading, and most non‑AI math.

​**Use case:** Any general parallel workload, classic rendering, many HPC‑style calculations.

**Tensor Cores**
* Specialized for AI and deep learning training and inference.
​* Perform matrix operations very efficiently, giving up to ~10× better performance on specific AI workloads compared to using only CUDA cores.
​
**Use case:** Neural network training, inference acceleration, features like DLSS (deep learning super sampling).

**RT (ray tracing) Cores**
* Dedicated to real‑time ray tracing and light simulation.
​* Compute realistic lighting, shadows, and reflections in games and visualization.
​
**Use case:** High‑fidelity real‑time graphics (e.g., modern AAA games, cinematic rendering).

