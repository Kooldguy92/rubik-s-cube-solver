#note you can mixed this with rubik cube solver program

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

# create a figure and set the background color to black
fig = plt.figure(figsize=(8, 8), facecolor='black')

# create a 3D axes object
ax = fig.add_subplot(111, projection='3d')

# set the limits of the axes
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# create the vertices of the cube
verts = [
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, 1],
    [-1, 1, 1],
    [1, 1, 1],
    [1, -1, 1]
]

# create the faces of the cube using the vertices
faces = [
    [0, 1, 2, 3],
    [3, 2, 6, 7],
    [7, 6, 5, 4],
    [4, 5, 1, 0],
    [1, 5, 6, 2],
    [4, 0, 3, 7]
]

# create a Poly3DCollection object with the faces and color it green
cube = [[verts[i] for i in face] for face in faces]
collection = Poly3DCollection(cube, facecolors='g')

# add the collection to the 3D axes object
ax.add_collection3d(collection)

# set the viewing angle
ax.view_init(elev=30, azim=-60)

# show the plot
plt.show()
