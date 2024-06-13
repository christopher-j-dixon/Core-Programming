import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x * y * np.exp(-2 * x**2 - y**4)

x = np.linspace(-1, 1, 1000)
y = np.linspace(-1, 1, 1000)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

contours = plt.contour(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()
plt.clabel(contours, inline=True, fontsize=8)

plt.title("Level Curves of $f(x, y) = xy e^{-2x^2 - y^4}$")
plt.xlabel("x")
plt.ylabel("y")

plt.savefig('outputimage.png')
plt.show()

# Define the function
def f(x, y):
    return x * y * np.exp(-2 * x**2 - y**4)

# Create the figure and 3D axes
fig = plt.figure()
ax = plt.axes(projection='3d')

# Generate the x and y data
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)

# Create the meshgrid for the x and y data
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Plot the surface
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot', edgecolor='none')
ax.set_title('Surface Plot of $f(x, y) = xy e^{-2x^2 - y^4}$')

# Set the axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Save the plot to a file
plt.savefig('outputimage.png')
plt.show()

def draw_plot(a, tmax, n):
    """
    Draw a 3D plot of a torus.

    Parameters:
    ----------
    a : float
        Angular frequency for the cosine function.
    tmax : float
        Maximum value of the parameter t.
    n : int
        Number of points to generate in the plot.
    """
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    t = np.linspace(0, tmax, n)
    x = np.cos(a * t)
    y = (4 + np.sin(a * t)) * np.cos(t)
    z = (4 + np.sin(a * t)) * np.sin(t)
    
    ax.plot(x, y, z, label='Torus')
    ax.legend()
    
    ax.set_title('3D Plot of a Torus')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

# Draw the plot with specified parameters
draw_plot(2 * np.pi, 20 * np.pi, 1000)

# Save the figure to a file
plt.savefig('outputimage.png')
plt.show()

### Give your answer here: ###
#
# Answer: The figure is a torus.
