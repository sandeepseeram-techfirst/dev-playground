### Job Scheduling vs. Container Orchestration 
Job scheduling is about optimally queuing and allocating long‑running, heavy training jobs to limited GPU/CPU nodes, while container orchestration is about keeping many short‑lived, containerized inference services healthy, balanced, and scalable.

#### Training vs Inference alignment

* **Job scheduling** aligns with model training: long‑running, resource‑intensive jobs needing predictable performance, high memory, and high GPU/CPU usage.​

* **Container orchestration** aligns with model inference: many concurrent, containerized microservices that must scale, stay healthy, and serve traffic continuously.
