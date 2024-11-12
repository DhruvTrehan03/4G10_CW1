import numpy as np
import cond_color
import matplotlib.pyplot as plt
import random

data = np.load('psths.npz')
X, times = data['X'], data['times']

print(np.shape(X), np.shape(times))

neurons = sorted(random.sample(range(0,np.shape(X)[0]-1),5))
print(neurons)
conditions = sorted(random.sample(range(0,np.shape(X)[1]-1),5))
print(conditions)

plt.figure(figsize=((15,15)))

for i, neuron in enumerate(neurons):
    for j, condition in enumerate(conditions):
        plt.subplot(len(neurons), len(conditions), i * len(conditions) + j + 1)
        plt.plot(times,X[neuron, condition, :], label=f'Neuron {neuron+1}, Cond {condition+1}')
        plt.axvline(0,'red')
        plt.tight_layout()

plt.show()