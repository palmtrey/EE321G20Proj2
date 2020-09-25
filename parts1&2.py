import matplotlib.pyplot as plt # For 2D plotting
from mpl_toolkits import mplot3d # For 3D plotting
import numpy as np # For MATHS

data = np.genfromtxt('gen_data.csv', delimiter=',') #ndarray from numpy

print("Shape of imported data: " + str(data.shape))

fig1 = plt.figure(figsize=(200, 3))
ax = plt.axes(projection="3d")

# Creating plot
ax.scatter3D(data[:, 0], data[:, 1], data[:, 2], color="green")
plt.title("gen_data in 3D")
#plt.show()

meanOfData = [data[:, 0].mean(), data[:, 1].mean(), data[:, 2].mean()]

demeanedData = [data - meanOfData]

transposedArray = np.transpose(demeanedData)

r = data[:, 0].size

print(r)

cd = (1/(r-1))*(transposedArray*demeanedData)

print(cd.shape)


#print(transposedArray)

#print(data.shape)
