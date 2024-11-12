import numpy as np
import cond_color
import matplotlib.pyplot as plt

data = np.load('psths.npz')
X, times = data['X'], data['times']

plt.plot(X[1])
