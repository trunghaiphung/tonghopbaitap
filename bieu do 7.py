import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
ax = plt.axes(projection="3d")
ax.scatter3D(weight,height)
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
plt.show()