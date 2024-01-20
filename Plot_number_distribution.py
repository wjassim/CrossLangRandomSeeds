import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Note: Seaborn library is used for plotting. Install it using:
# pip install seaborn


# Set the size of the sample
size = 10000

# Set the random seed for reproducibility
np.random.seed(42)

# Generate random numbers from a uniform distribution (0 to 1)
x1 = np.random.rand(size)

# Plot histogram with kernel density estimate (KDE) and statistical elements
plt.figure()
sns.histplot(
    x1,
    fill=True,
    alpha=0.2,
    bins=20,
    kde=True,
    element="step",
)
plt.axvline(x=x1.std(), linestyle="-.", color="green", label="std = {:.3f}".format(x1.std()))
plt.axvline(x=x1.mean(), linestyle="-.", color="red", label="mean = {:.3f}".format(x1.mean()))
plt.title("Uniform Distribution - Original")
plt.legend()
# plt.grid()  # Uncomment this line if you want to include grid lines
plt.show()

# Plot histogram with KDE and independent density normalization
plt.figure()
sns.histplot(
    x1,
    fill=True,
    alpha=0.2,
    bins=20,
    kde=True,
    element="step",
    stat="density",
)
plt.axvline(x=x1.std(), linestyle="-.", color="green", label="std = {:.3f}".format(x1.std()))
plt.axvline(x=x1.mean(), linestyle="-.", color="red", label="mean = {:.3f}".format(x1.mean()))
plt.title("Uniform Distribution - With Density Normalization")
plt.legend()
plt.show()

# Generate random numbers from a uniform distribution in the range [-1, 1]
a, b = -1.0, 1.0
np.random.seed(42)
x2 = np.random.uniform(low=a, high=b, size=size)

# Plot histogram with KDE, step filling, and no common normalization
plt.figure()
sns.histplot(
    x2,
    fill=True,
    alpha=0.2,
    bins=20,
    kde=True,
    element="step",
    common_norm=False,
)
plt.axvline(x=x2.std(), linestyle="-.", color="green", label="std = {:.3f}".format(x2.std()))
plt.axvline(x=x2.mean(), linestyle="-.", color="red", label="mean = {:.3f}".format(x2.mean()))
plt.title("Uniform Distribution - Ranged")
plt.legend()
plt.show()
