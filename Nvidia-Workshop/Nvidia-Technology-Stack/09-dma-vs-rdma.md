### DMA vs. RDMA 
DMA and RDMA are about moving data without wasting CPU time.

**DMA:** skip the CPU inside one machine.
​**RDMA:** skip the CPU across machines over the network.


Host 1                              Host 2
------                              ------
GPU / Device                        GPU / Device
   |                                   |
  DMA                                 DMA
   |                                   |
 RDMA NIC  <====== RDMA fabric =====> RDMA NIC
                      (InfiniBand / RoCE / etc.)
                    directly accesses
                   Host 2's memory

CPU involvement: mainly for setup & control, not for bulk data copy.
