#Credit goes to Dr. Huixia Lu, 02 June 2025
import numpy as np
import matplotlib.pyplot as plt

def fibonacci_sphere_points(N, radius=1.0):
    points = []
    golden_angle = np.pi * (3 - np.sqrt(5))  # ~2.39996

    for i in range(N):
        z = 1 - (2 * i) / (N - 1)  # z from 1 to -1
        theta = golden_angle * i
        xy_radius = np.sqrt(1 - z**2)

        x = np.cos(theta) * xy_radius
        y = np.sin(theta) * xy_radius

        # Scale by radius
        points.append((radius * x, radius * y, radius * z))
    return np.array(points)

# Parameters
N = 200
r = 10.0

# Generate points
points = fibonacci_sphere_points(N, r)

#save the generated points into xxx.dat file:
np.savetxt("points_coor.dat", points, fmt="%.6f", delimiter="\t", header="# x_coor y_coor z_coor", comments="")

# Plotting
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=4)
ax.set_box_aspect([1, 1, 1])
plt.savefig("points.png", dpi=300, bbox_inches='tight')
plt.show()
