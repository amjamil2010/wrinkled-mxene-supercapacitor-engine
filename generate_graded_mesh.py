import numpy as np

print("--- STARTING PHASE 2: LOGARITHMIC MESH CONFIGURATION ---")

# 1. Define channel physical dimensions (in nanometers)
channel_width = 10.0  # Total distance from electrode into the bulk fluid
num_nodes = 150       # Number of points along the line

# 2. Apply logarithmic stretching function toward the interface (x = 0)
# This concentrates nodes heavily within the first 1.0 nm boundary layer
mesh_points = np.logspace(np.log10(0.05), np.log10(channel_width + 0.05), num_nodes) - 0.05

# 3. Verify mesh resolution rules from the proposal
near_wall_resolution = mesh_points[1] - mesh_points[0]
bulk_resolution = mesh_points[-1] - mesh_points[-2]

print(f"Total Grid Nodes Generated: {len(mesh_points)}")
print(f"Resolution at Active Interface (Goal <= 0.05nm): {near_wall_resolution:.4f} nm")
print(f"Resolution in Bulk Fluid Domain (Goal ~ 2.0nm): {bulk_resolution:.4f} nm")

# 4. Save the coordinates to be loaded directly by our continuum solver
np.savetxt('graded_mesh_coordinates.txt', mesh_points, header='Grid_Node_X_Coordinates_nm')
print("--- SUCCESS: graded_mesh_coordinates.txt has been locked and loaded! ---")