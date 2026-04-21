import numpy as np

y = np.load("data/y.npy")

print("Total samples:", len(y))
print("Left (-1):", np.sum(y == -1))
print("Right (1):", np.sum(y == 1))
print("Straight (0):", np.sum(y == 0))



