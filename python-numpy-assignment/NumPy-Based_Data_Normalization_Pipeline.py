import numpy as np

# 1. Create a NumPy array (numeric feature values)
data = np.array([10, 20, 30, 40])

# 2. Compute mean and standard deviation
mean = np.mean(data)
std = np.std(data)

# 3. Normalize the data
normalized = (data - mean) / std

# 4. Reshape into 2D array (2 rows, 2 columns)
reshaped = normalized.reshape(2, 2)

# 5. Print results
print("Original array:", data)
print("Mean:", mean)
print("Standard deviation:", std)
print("Normalized array:", normalized)
print("Reshaped array:\n", reshaped)
print("Reshaped shape:", reshaped.shape)