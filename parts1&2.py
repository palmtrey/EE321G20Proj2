# Title: Parts 1 & 2
# Purpose: To fulfill parts 1 and 2 of project 2 of EE 321: Systems and Signal Processing
# Developers: Shawn Boyd, Cameron Palmer, Siddesh Sood
# Last Modified: September 29th, 2020

# Importing libraries
import matplotlib.pyplot as plt  # For 2D plotting
import numpy as np  # For MATHS

## 1 Examine the data

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


## 2 Dimensionality reduction

## 2.1 Principle Component Analysis (PCA)
r = data[:, 0].size  # r = 200

# Find the mean of the data
meanOfData = np.mean(data, axis = 0)

# Demean the data
demeanedData = [np.asarray(data) - np.asarray(meanOfData)]  # Yields an array of shape (1, 200, 3)
demeanedDataProper = np.squeeze(np.asarray(demeanedData))  # Gets rid of the third dimension of size 1. New shape is (200, 3)

#print("Shape of demeaned data: " + str(demeanedDataProper.shape))

transposedArray = np.transpose(demeanedDataProper)

#print("Shape of transposed array: " + str(transposedArray.shape))

cd = (1/(r-1))*(np.dot(transposedArray, demeanedDataProper))

# Calculate qd and dd
dd, qd = np.linalg.eig(cd) # qd eigenvectors, dd eigenvalues

print("qd: " + str(qd))
print("dd: " + str(dd))


## 2.2 Dimensionality

# Sorting eigenvalues
sorted_eig_vals = np.sort(np.diag(dd))

print(sorted_eig_vals)

eig_val_ind = np.where(sorted_eig_vals == np.max(sorted_eig_vals, axis = 1))



#print(np.amax(sorted_eig_vals, axis = 1))












# Finding the eigenvector corresponding to the highest eigenvalue
eigen_vec_to_use = qd[np.where(dd == np.amax(dd))]

#print(np.transpose(eigen_vec_to_use))

#reconstructed_data = np.dot(np.squeeze(np.transpose(eigen_vec_to_use)),data)
#print(reconstructed_data)

#print("Before: " + str(ind))
#print("eig_val_sorted: " + str(eig_val_sorted))
