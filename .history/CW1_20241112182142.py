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