import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
square = patches.Rectangle((0, 0), 1, 1, edgecolor='orange', facecolor='none')
ax.add_patch(square)
plt.xlim(-0.5, 5.5)
plt.ylim(-0.5, 5.5)
plt.gca().set_aspect('equal', adjustable='box') # Ensures equal aspect ratio
plt.title('Square Plot with add_patch()')
plt.show()
