import numpy as np

data = np.load('psths.npz')
X, times = data['X'], data['times']

print(np.shape(X),times)