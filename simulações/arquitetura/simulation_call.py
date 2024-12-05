import numpy as np
import matplotlib.pyplot as plt
import os
import importlib.util


module_name = 'lumapi'
module_path = r'C:\Program Files\Lumerical\v241\api\python\lumapi.py'

os.add_dll_directory(r'C:\Program Files\Lumerical\v241\api\python')

# Find the module specification
spec = importlib.util.spec_from_file_location(module_name, module_path)

#print(spec)
# Create a module from the specification
lumapi = importlib.util.module_from_spec(spec)

# Load the module into the current namespace
spec.loader.exec_module(lumapi)



matrix_size = 10
unit_y_size = 0.9*10**-6
unit_z_size = 0.9*10**-6
block_y_size = unit_y_size/matrix_size
block_z_size = unit_z_size/matrix_size

design_matrix = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])
print(design_matrix.shape)
#design_matrix = np.random.randint(2, size=(matrix_size, matrix_size))
print(design_matrix)

simu = lumapi.FDTD(filename="substrate.fsp", hide=False)


simu.addstructuregroup(name="surface")
for i in range(design_matrix.shape[0]):
    for j in range(design_matrix.shape[1]):
        if design_matrix[j,i] == 1:
            z_position = -i*block_z_size + unit_z_size/2
            y_position = j*block_y_size - unit_y_size/2


            simu.addrect(name=f"block_{i}_{j}")
            # Set the boundaries
            simu.set("x min", -.02e-6)  # Minimum x-coordinate
            simu.set("x max", 0)   # Maximum x-coordinate
            simu.set("y min", y_position)  # Minimum y-coordinate
            simu.set("y max", y_position + block_y_size)   # Maximum y-coordinate
            simu.set("z min", z_position - block_z_size)  # Minimum z-coordinate
            simu.set("z max", z_position)   # Maximum z-coordinate
            simu.addtogroup("surface")

input()
 

