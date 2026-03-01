import numpy as np

np.random.seed(42)

data = np.random.randn(100, 5)
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

normalized = (data - mean) / std

split_index = int (0.8 * len(normalized))
train = normalized[:split_index]
test = normalized[split_index:]

train[0,0] = 999

print ("Original data shape:", data.shape)
print ("Mean shape:", mean.shape)
print("Standard deviation shape:", std.shape)
print("Training set shape:", train.shape)
print("Testing set shape:", test.shape)

print("\nAfter modifying the training [0,0]:")
print("Normalized data [0,0]:", normalized[0,0])
print("Change observed because slicing returns a view, not a copy.")