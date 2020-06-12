import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

area = 300  # Planned purchase area
mouth = 1200  # Expected investment period
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(0, area, 10)
Y = np.arange(0, mouth, 40)
X, Y = np.meshgrid(X, Y)
Z = X * Y / 300 - 2 * X

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
