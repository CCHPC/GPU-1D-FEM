# GPU-1D-FEM
Simple 1 dimensional finite element forced convection heat equation solution on the GPU

The problem solved is described in the comment block at the start of main{} in femHeat.cu.  The values of thermal conductivity, K, 
strength of advection, M (= rho Cp Ux), the source strength, S0, and domain length, L as well as the number of finite elements, E, in
the solution all can be varied.  E is an integer, but the rest are doubles.  M and S0 may be negative. If you change a number simply 
recompile the code: ./compile_it and then run it: ./run_it.  Results are written to the output directory and includes the solution 
vector along with the exact solution at each node location (exact solution is NOT a smooth function at coarser resolutions).  Other 
solution info is also shown in the output directory.  Data in the output directory initially are for E = 20, K = 1., M = 10., S0 = 4., 
and L = 1. The .pdf is a plot of this solution.

This FEM code is based, in part, upon a CUDA Ax=b code found at:

https://stackoverflow.com/questions/28794010/solving-dense-linear-systems-ax-b-with-cuda

