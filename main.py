from math import degrees, cos, sin
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from Kinematics import Kinematics
# from AnglePlot import get_angle_plot

if __name__ == '__main__':
    l1 = float(input('Ingrese la longitud del brazo 1: '))
    l2 = float(input('Ingrese la longitud del brazo 2: '))
    px = float(input('Ingrese la coordenada x del punto p: '))
    py = float(input('Ingrese la coordenada y del punto p: '))
    plot_limit = l1 + l2

    model = Kinematics(l1, l2)
    theta1, theta2 = model.makeInverse(px, py)
    print(degrees(theta1), degrees(theta2))

    x0 = 0
    y0 = 0
    x1 = l1*cos(theta1)
    y1 = l1*sin(theta1)
    x2 = x1+l2*cos(theta1+theta2)
    y2 = y1+l2*sin(theta1+theta2)
    x3 = x1+l2*cos(theta1)
    y3 = y1+l2*sin(theta1)

    fig = plt.figure()
    ax = fig.add_subplot(
        1, 1, 1, xlim=(-plot_limit, plot_limit), ylim=(-plot_limit, plot_limit))

    line_1 = Line2D([x0, x1], [y0, y1], linewidth=1,
                    linestyle="-", color="blue")
    line_2 = Line2D([x1, x2], [y1, y2], linewidth=1,
                    linestyle="-", color="cyan")
    line_3 = Line2D([x1, x3], [y1, y3], linewidth=1,
                    linestyle="--", color="cyan", alpha=0.2)

    ax.add_line(line_1)
    ax.add_line(line_2)
    ax.add_line(line_3)
    ax.plot(px, py, 'o', color='m')
    ax.grid()

    plt.show()
