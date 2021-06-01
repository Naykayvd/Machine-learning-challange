# Nahum Van Diemen
import numpy as np
import matplotlib.pyplot as plt

nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print("nums: ", nums)
print("bins: ", bins)
print("Result:", np.histogram(nums, bins))
plt.xlabel("numbers")
plt.ylabel("bins")
plt.title("numbers against bins")
plt.hist(nums, bins=bins)
plt.show()
