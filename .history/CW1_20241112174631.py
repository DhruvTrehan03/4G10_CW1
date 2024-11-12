import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.load('psths.npz')
X, times = data['X'], data['times']  # Extract the PSTH data and time labels

# Parameters
N, C, T = X.shape  # Get the dimensions (neurons, conditions, time bins)
print(f"Data dimensions: N={N}, C={C}, T={T}")
print(f"Time range: {times[0]} ms to {times[-1]} ms")

# Subset selection
selected_neurons = [0, 1, 2, 3, 4]  # Example: first 5 neurons
selected_conditions = [0, 1, 2]  # Example: first 3 conditions

# Plotting PSTHs for selected neurons and conditions
plt.figure(figsize=(15, 10))
for i, neuron in enumerate(selected_neurons):
    for j, condition in enumerate(selected_conditions):
        plt.subplot(len(selected_neurons), len(selected_conditions), i * len(selected_conditions) + j + 1)
        plt.plot(times, X[neuron, condition, :], label=f'Neuron {neuron+1}, Cond {condition+1}')
        plt.axvline(0, color='red', linestyle='--', label='Movement Onset')
        plt.xlabel('Time (ms)')
        plt.ylabel('Firing Rate (Hz)')
        plt.title(f'Neuron {neuron+1}, Condition {condition+1}')
        plt.legend()
        plt.tight_layout()

plt.show()
