import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert input list to a 3x3 Numpy array
    array = np.array(input_list).reshape(3, 3)

    # Perform calculations
    calculations = {
        'mean': [
            np.mean(array, axis=0).tolist(),
            np.mean(array, axis=1).tolist(),
            np.mean(array).tolist()
        ],
        'variance': [
            np.var(array, axis=0).tolist(),
            np.var(array, axis=1).tolist(),
            np.var(array).tolist()
        ],
        'standard deviation': [
            np.std(array, axis=0).tolist(),
            np.std(array, axis=1).tolist(),
            np.std(array).tolist()
        ],
        'max': [
            np.max(array, axis=0).tolist(),
            np.max(array, axis=1).tolist(),
            np.max(array).tolist()
        ],
        'min': [
            np.min(array, axis=0).tolist(),
            np.min(array, axis=1).tolist(),
            np.min(array).tolist()
        ],
        'sum': [
            np.sum(array, axis=0).tolist(),
            np.sum(array, axis=1).tolist(),
            np.sum(array).tolist()
        ]
    }

    return calculations
