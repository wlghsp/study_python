import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

z = np.arrange(-7, 7, 0.1)
f_x = sigmoid(z)

plt.plot(z, f_x)
plt.axvline(0.0, color = 'k')
plt.ylim(-0.1, 1, 1, 1)
plt.xlabel('z')
plt.ylabel('f(x)')

plt.yticks([0.0, 0.5, 1.0])
ax = plt.gca()
ax.yaxis.grid(True)
plt.tight_layout()
plt.show()
