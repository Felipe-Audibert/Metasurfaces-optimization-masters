import numpy as np
import matplotlib.pyplot as plt
from sko.GA import GA
from simulation_call_rings import rings_simulation
from datetime import datetime
import json

print("beginning:", datetime.now())

# Ensure all numpy arrays are converted to lists for JSON serialization
def convert_to_serializable(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, list):
        return [convert_to_serializable(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    return obj

counter = 0

# Define the fitness function
def fitness_function(x):
    global counter
    counter += 1
    print(counter)
    T = rings_simulation(x)
    return np.sum(1-(1-np.abs(T["T"])))

# Parameters
num_generations = 25
num_genes = 4
population_size = 20

# Initialize GA
ga = GA(func=fitness_function, n_dim=num_genes, size_pop=population_size, max_iter=num_generations, lb=[0, 0, 0, 0], ub=[1, 1, 1, 1], prob_mut=0.05)

# Run the GA
best_x, best_y = ga.run()

print("ending:", datetime.now())

plt.plot(ga.generation_best_Y)
plt.show()

print("Best solution : ", best_x)
print("Best solution fitness : ", best_y)

ga_outputs = {
    'generation_best_Y': ga.generation_best_Y,
    'generation_best_X': ga.generation_best_X,
    'all_history_FitV': ga.all_history_FitV,
    'all_history_Y': ga.all_history_Y,
    'best_solution': best_x,
    'best_objective_value': best_y
}

# Convert the dictionary to a serializable format
serializable_dict = convert_to_serializable(ga_outputs)

# Save the dictionary to a JSON file
with open('ga_outputs.json', 'w') as json_file:
    json.dump(serializable_dict, json_file, indent=4)