# Title: Parts 1 & 2
# Purpose: To fulfill parts 1 and 2 of project 2 of EE 321: Systems and Signal Processing
# Developers: Shawn Boyd, Cameron Palmer, Siddesh Sood
# Last Modified: September 29th, 2020

import matplotlib.pyplot as plt  # For 2D plotting
from mpl_toolkits import mplot3d  # For 3D plotting
import numpy as np  # For MATHS

# Import the data from the csv file
data = np.genfromtxt('gen_data.csv', delimiter=',') #ndarray from numpy

# Print out the shape of the imported data
print("Shape of imported data: " + str(data.shape))

# Creating plot
fig1 = plt.figure(figsize=(200, 3))
ax = plt.axes(projection="3d")
ax.scatter3D(data[:, 0], data[:, 1], data[:, 2], color="green")
plt.title("gen_data in 3D")
#plt.show()


r = data[:, 0].size  # r = 200

# Find the mean of the data
meanOfData = np.mean(data, axis = 0)
print("Mean of the data: " + str(meanOfData))

# Demean the data
demeanedData = [np.asarray(data) - np.asarray(meanOfData)]  # Yields an array of shape (1, 200, 3)
demeanedDataProper = np.squeeze(np.asarray(demeanedData))  # Gets rid of the third dimension of size 1. New shape is (200, 3)


print("Shape of demeaned data: " + str(demeanedDataProper.shape))


transposedArray = np.transpose(demeanedDataProper)


print("Shape of transposed array: " + str(transposedArray.shape))


cd = (1/(r-1))*(transposedArray*demeanedDataProper)

#print("Shape of cd: " + str(cd.shape))

A = np.array([[5, 3, 4], [3, 1, 3]])
B = np.array([1, 2, 3])

print(cd.shape)

#print(np.linalg.eigvals(np.diag(B)))

cd[:, :, 3:200] = 0

print(cd.shape)

#print(np.linalg.eig(cd))

#np.linalg.eigh(cd)


#print(transposedArray)

#print(data.shape)



