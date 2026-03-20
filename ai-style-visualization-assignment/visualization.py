import numpy as np
import matplotlib.pyplot as plt

# 1. Create a list of 10 epochs from 1 to 10
epochs = np.arange(1, 11)

# 2. Generate synthetic training loss values using NumPy
loss = np.array([0.95, 0.88, 0.82, 0.76, 0.69, 0.63, 0.58, 0.52, 0.47, 0.41])

# 3A. Line Plot: Epoch vs Loss
plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker='o')
plt.title("Training Loss Over Epochs")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 3B. Scatter Plot: Epoch vs Loss
plt.figure(figsize=(8, 5))
plt.scatter(epochs, loss)
plt.title("Scatter Plot of Epoch vs Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 4. Bar Chart comparing model accuracy
models = ['Model A', 'Model B', 'Model C']
accuracy = [0.92, 0.95, 0.89]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy)
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.grid(True, axis='y')
plt.show()