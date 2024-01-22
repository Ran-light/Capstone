# support function for interpolation
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import os

# Get bbox


def get_bbox(directory):
    bboxes: {str: tuple[int, ...]} = dict()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                for line in f:
                    label, x, y, width, height = line.split()
                    bboxes[filename] = (x, y, width, height, label)
    return bboxes

# Plots the piecewise connected function that consists of pieces of lagrange polynomials
# that consider a certain number of bbox locations for certain value types


def plot_piecewise_lagrange(frames_per_piece: int, bboxes, value_type: int):
    t_train = range(0, len(bboxes), 4)
    values = [float(list(bboxes.values())[i][value_type]) for i in t_train]

    plt.figure(figsize=(10, 5))
    plt.title("Piecewise Lagrange")
    plt.xlim(0, len(bboxes))
    plt.xlabel('frame')
    if value_type <= 1:
        plt.ylabel('position')
        plt.ylim(0, 1)
    elif value_type <= 3:
        plt.ylabel('size')
        plt.ylim(0, 0.3)
    plt.scatter(range(0, len(bboxes), 4), values)
    for i in range((len(t_train) + 4) // frames_per_piece):
        poly = lagrange(list(t_train)[frames_per_piece * i: frames_per_piece * i + frames_per_piece + 1]
                        , values[frames_per_piece * i: frames_per_piece * i + frames_per_piece + 1])
        x_new = np.arange((frames_per_piece * i) * 4, (frames_per_piece * i + frames_per_piece) * 4, 0.1)
        plt.plot(x_new, Polynomial(poly.coef[::-1])(x_new))

    plt.show()


def plot_piecewise_lagrange_3d(frames_per_piece: int, bboxes):
    t_train = range(0, len(bboxes), 4)
    x_spoon_train = [float(list(bboxes.values())[i][0]) for i in t_train]
    y_spoon_train = [float(list(bboxes.values())[i][1]) for i in t_train]

    fig = plt.figure(figsize=(10, 10))
    plt.title("Piecewise Lagrange")
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('t')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, len(bboxes))

    for i in range((len(t_train) + 4) // frames_per_piece - 1):
        x_poly = lagrange(list(t_train)[frames_per_piece * i: frames_per_piece * i + frames_per_piece + 1]
                          , x_spoon_train[frames_per_piece * i: frames_per_piece * i + frames_per_piece + 1])
        y_poly = lagrange(list(t_train)[frames_per_piece * i: frames_per_piece * i + frames_per_piece + 1]
                          , y_spoon_train[frames_per_piece * i: frames_per_piece * i + frames_per_piece + 1])

        t_new = np.arange((frames_per_piece * i) * 4, (frames_per_piece * i + frames_per_piece) * 4, 0.1)
        ax.plot(Polynomial(x_poly.coef[::-1])(t_new), Polynomial(y_poly.coef[::-1])(t_new), t_new)

    plt.show()
