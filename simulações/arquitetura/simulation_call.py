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



simu = lumapi.FDTD(filename="substrate.fsp", hide=False)
#simu.close()
#simu.addfdtd()
#simu.addmesh()
#simu.addrect()
#simu.save()
input()
 

