import numpy as np

# Given data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12, 16, 18])

# Calculate the means
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate b1 (slope)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
b1 = numerator / denominator

# Calculate b0 (intercept)
b0 = y_mean - b1 * x_mean

# Print the coefficients
print("b0 (intercept):", b0)
print("b1 (slope):", b1)
