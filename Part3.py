# Title: Part 3
# Purpose: To fulfill parts 1 and 3 of project 2 of EE 321: Systems and Signal Processing
# Developers: Shawn Boyd, Cameron Palmer, Siddesh Sood
# Last Modified: October 2, 2020

# Importing libraries
import matplotlib.pyplot as plt  # For 2D plotting
import numpy as np  # For MATHS

## 1 Examine the data

# Import the data from the csv file
data = np.genfromtxt('gen_data2.csv', delimiter=',') #ndarray from numpy

# Print out the shape of the imported data
print("Shape of imported data: " + str(data.shape))

# Creating plot
fig1 = plt.figure(figsize=(300, 3))
ax = plt.axes(projection="3d")
ax.scatter3D(data[:, 0], data[:, 1], data[:, 2], color="green")
plt.title("gen_data2 in 3D")
plt.show()


## 2 Dimensionality reduction

## 2.1 Principle Component Analysis (PCA)
r = data[:, 0].size  # r = 300

# Find the mean of the data
meanOfData = np.mean(data, axis = 0)

# Demean the data
demeanedData = [np.asarray(data) - np.asarray(meanOfData)]  # Yields an array of shape (1, 300, 3)
demeanedDataProper = np.squeeze(np.asarray(demeanedData))  # Gets rid of the third dimension of size 1. New shape is (300, 3)

transposedArray = np.transpose(demeanedDataProper)

cd = (1/(r-1))*(np.dot(transposedArray, demeanedDataProper))

# Calculate qd and dd
dd, qd = np.linalg.eig(cd) # qd eigenvectors, dd eigenvalues

print("qd: " + str(qd))
print("dd: " + str(dd))


## 2.2 Dimensionality

# Sorting eigenvalues if needed np.linalg.eig sorts by descending order
#sorted_eig_vals = np.sort(np.diag(dd))
#print("Sorted DD:" + str(sorted_eig_vals))
#eig_val_ind = np.where(sorted_eig_vals == np.max(sorted_eig_vals, axis = 1))
#print("Indices:"+ str(eig_val_ind))
#print(np.where(sorted_eig_vals))
# print(np.amax(sorted_eig_vals, axis = 1))


#Selecting the eigenvector corresponding to the highest valued eigenvalue
num_comp = 1
prin_comps = qd[:, [0]]

reconstructed_data = np.dot(data, (prin_comps))

y = np.zeros((300, 1))


#Scatter Plot
plt.figure(0)
plt.scatter(reconstructed_data, y)
plt.title('Part 3: Reconstructed data projected onto one dimension')
plt.show()
