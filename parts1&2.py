import matplotlib.pyplot as plt # For 2D plotting
from mpl_toolkits import mplot3d # For 3D plotting
import numpy as np # For MATHS

data = np.genfromtxt('gen_data.csv', delimiter=',') #ndarray from numpy

fig1 = plt.figure(figsize=(200, 3))
ax = plt.axes(projection="3d")

# Creating plot
ax.scatter3D(data[:, 0], data[:, 1], data[:, 2], color="green")
plt.title("gen_data in 3D")
#plt.show()

meanOfData = [data[:, 0].mean(), data[:, 1].mean(), data[:, 2].mean()]

demeanedData = [data - meanOfData]

print(meanOfData)

print(demeanedData)

#print(data.shape)
