import numpy as np

# 1. Setup the potential window (-1.5 V to +1.5 V with 51 points)
potentials = np.linspace(-1.5, 1.5, 51)

# 2. Define physical constants
e = 1.602e-19       # Elementary charge (Coulombs)
kb = 1.381e-23      # Boltzmann constant (J/K)
T = 298.15          # Temperature (Kelvin)
EF = 0.0            # Fermi level reference (eV)

# 3. Model a baseline Density of States (DOS) for Ti3C2O2
# This represents the localized state-counting distribution near the Fermi level
def baseline_dos(E):
    return 1e18 * (1.0 + 0.5 * np.exp(-((E - 0.2) / 0.1)**2))

# 4. Compute the Fermi-Dirac distribution
def fermi_dirac(E, phi):
    # Shifted by the local electrostatic potential
    energy_diff = (E - (EF - phi)) * e
    # Prevent overflow bugs in exponential calculations
    val = np.clip(energy_diff / (kb * T), -100, 100)
    return 1.0 / (1.0 + np.exp(val))

# 5. Calculate integrated quantum surface charge density
sigma_quantum = []
energy_grid = np.linspace(-2.0, 2.0, 1000) # Integration energy range in eV

for phi in potentials:
    # Evaluate the integrand: DOS(E) * Fermi-Dirac(E, phi)
    integrand = [baseline_dos(E) * fermi_dirac(E, phi) for E in energy_grid]
    # Perform numerical integration using the trapezoidal rule
    integrated_val = np.trapz(integrand, energy_grid)
    # Apply charge scaling
    charge = -e * integrated_val
    sigma_quantum.append(charge)

# 6. Save the data into a clean 1D tabulated array text file
output_data = np.column_stack((potentials, sigma_quantum))
np.savetxt('quantum_charge_profile.txt', output_data, header='Potential(V) Sigma_Quantum(C/m2)')

print("\n--- SUCCESS: quantum_charge_profile.txt has been generated with 51 data points! ---")
