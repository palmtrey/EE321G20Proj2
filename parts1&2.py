import matplotlib.pyplot as plt # For 2D plotting
from mpl_toolkits import mplot3d # For 3D plotting
import numpy as np # For MATHS

data = np.genfromtxt('gen_data.csv', delimiter=',')

fig1 = plt.figure(figsize=(200, 3))
ax = plt.axes(projection="3d")

# Creating plot
ax.scatter3D(data[:, 0], data[:, 1], data[:, 2], color="green");
plt.title("gen_data in 3D")
plt.show()

print(data.shape)
