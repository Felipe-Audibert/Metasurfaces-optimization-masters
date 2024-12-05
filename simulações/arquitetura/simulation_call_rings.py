import numpy as np
import matplotlib.pyplot as plt
import os
import importlib.util


def rings_simulation(rings):
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



    unit_y_size = 0.9*10**-6
    unit_z_size = 0.9*10**-6
    margin_size = 0.09*10**-6

    monitor_name = "reflection"

    simu = lumapi.FDTD(filename="substrate.fsp", hide=False)

    simu.addstructuregroup(name="surface")
    simu.set("x",0)
    simu.set("y",0)
    simu.set("z", 0)   

    for ring in range(len(rings)):
        if rings[ring] >= .25: 
            interval = (unit_y_size-margin_size*2)/(2*4)
            simu.addring(name=f"ring_{ring}")
            simu.set("x",0)
            simu.set("y",0)
            simu.set("z", 0)
            simu.set("z span",0.02e-6)
            simu.set("inner radius",interval*(ring + 1) - rings[ring]*interval*.8)
            simu.set("outer radius",interval*(ring + 1))
            simu.set("second axis", "y")
            simu.set("rotation 2", 90)
            simu.set("x",-0.01e-6)
            simu.addtogroup("surface")


    simu.run()

    # Get the frequency or wavelength data
    #wavelength = simu.getdata(source_name, "wavelength")  # or use "frequency" for frequency data

    # Get the transmission data
    T = simu.getresult(monitor_name,"T")


    # For demonstration, plot the transmission spectrum
    
    
    plt.plot( T["lambda"], 1-abs(T["T"]), label='Transmission')
    plt.xlabel('Wavelength (m)')
    plt.ylabel('Transmission')
    plt.title('Transmission Spectrum')
    plt.legend()
    plt.grid(True)
    plt.show()
    print(np.sum(1-(1-np.abs(T["T"]))))
    


    simu.switchtolayout()
    simu.select("surface")
    simu.delete()
    simu.save()
    
 

    return T



if __name__ == "__main__":

    result = rings_simulation(np.array([
        0.9670883397512638,
        0.9815431822266091,
        0.9998729228897645,
        0.9393533432098236
    ]))
    input()
