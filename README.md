# Wrinkled MXene Supercapacitor Electrodes Engine

A resource-efficient, self-consistent multiscale computational framework solved in FEniCSx. This engine couples database-mined Density Functional Theory (DFT) and semi-empirical Density Functional Tight-Binding (DFTB+) structures with a Bikerman-Kornyshev Modified Poisson-Boltzmann (MPB) model under a strict memory envelope (< 1.5 GB RAM).

## Code Structure & Pipeline

Run the scripts sequentially to reproduce the computational data:
1. `1_quantum_charge_profile.py` - Generates the potential-dependent quantum excess surface charge density array.
2. `2_graded_mesh_configuration.py` - Sets up the logarithmic boundary layer mesh grading.
3. `3_multiscale_solver_engine.py` - Executes the core non-linear coupled solver sweeps using a three-tier convergence stabilization protocol (PETSc GMRES + ILU0).
4. `4_corrugated_wrinkle_analysis.py` - Maps local geometric strains and structural calibration matrices.
5. `5_final_extractor_metrics.py` - Computes global differential capacitance limits and extracts multi-model thermodynamic variance profiles.

## Citation Required

If you utilize this framework, adapt these scripts, or use our tabulated configurations to optimize your computational constraints, you are required to cite our primary paper:

```text
Jamil, A. M. (2026). Decoupling Quantum Capacitance and Interfacial Dielectric Saturation in Wrinkled MXene Supercapacitor Electrodes: A Resource-Efficient Multiscale Computational Framework. ChemRxiv Preprint.
