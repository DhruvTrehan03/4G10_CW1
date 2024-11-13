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
avg_firing_rate = X.mean(axis=(0,1))
plt.figure(figsize=((15,15)))

for i, neuron in enumerate(neurons):
    for j, condition in enumerate(conditions):
        plt.subplot(len(neurons), len(conditions), i * len(conditions) + j + 1)
        plt.plot(times,X[neuron, condition, :], label=f'Neuron {neuron+1}, Cond {condition+1}')
        plt.plot(times, avg_firing_rate)
        plt.axvline(0,color = 'red', linestyle = '--', label = 'Movement Offset')
        plt.xlabel('Time(ms)')
        plt.ylabel('Firing Rate (Hz)')
        plt.title(f'Neuron {neuron +1}, Condition {condition + 1}')


plt.tight_layout()
plt.show()