from sklearn.datasets import make_moons

X, y = make_moons(n_samples =200,
                  noise = 0.05,
                  random_state= 0)

import matplotlib.pyplot as plt

plt.scatter(X[:,0], X[:,1])
plt.tight_layout()
plt.show()