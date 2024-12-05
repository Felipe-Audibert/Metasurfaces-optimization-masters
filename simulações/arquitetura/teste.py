import json
import numpy as np

with open('ga_outputs.json', 'r') as json_file:
    ga_outputs = json.load(json_file)

'''
ga_outputs = {
    'generation_best_Y': [1.0, 0.5, 0.2],
    'generation_best_X': [[1, 2], [3, 4], [5, 6]],
    'all_history_FitV': [[0.9, 0.8], [0.7, 0.6], [0.5, 0.4]],
    'all_history_Y': [[0.9, 0.8], [0.7, 0.6], [0.5, 0.4]],
    'best_solution': [1, 2],
    'best_objective_value': 0.1
}

# Ensure all numpy arrays are converted to lists for JSON serialization
def convert_to_serializable(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, list):
        return [convert_to_serializable(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    return obj

# Convert the dictionary to a serializable format
serializable_dict = convert_to_serializable(ga_outputs)

# Save the dictionary to a JSON file
with open('ga_outputs.json', 'w') as json_file:
    json.dump(serializable_dict, json_file, indent=4)
'''

print(ga_outputs)