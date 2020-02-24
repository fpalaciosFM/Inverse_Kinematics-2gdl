from math import degrees, cos, sin, sqrt
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.lines import Line2D
from Kinematics import Kinematics
# from AnglePlot import get_angle_plot, get_angle_text
from matplotlib.patches import Arc
import random


def distancia(x1, y1, x2, y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)


def plotInverseK(l1, l2, px, py):
    plot_limit = l1 + l2

    model = Kinematics(l1, l2)
    theta1, theta2 = model.makeInverse(px, py)
    theta1 = -theta1 if False else theta1

    x0 = 0
    y0 = 0
    x1 = l1*cos(theta1)
    y1 = l1*sin(theta1)
    x2 = x1+l2*cos(theta1+theta2)
    y2 = y1+l2*sin(theta1+theta2)
    x3 = x1+l2*cos(theta1)
    y3 = y1+l2*sin(theta1)

    if distancia(px, py, x2, y2) > 0.0001:
        theta1 = -theta1
        x0 = 0
        y0 = 0
        x1 = l1*cos(theta1)
        y1 = l1*sin(theta1)
        x2 = x1+l2*cos(theta1+theta2)
        y2 = y1+l2*sin(theta1+theta2)
        x3 = x1+l2*cos(theta1)
        y3 = y1+l2*sin(theta1)

    print(degrees(theta1), degrees(theta2))

    fig = plt.figure()
    ax = fig.add_subplot(
        1, 1, 1, xlim=(-plot_limit, plot_limit), ylim=(-plot_limit, plot_limit))

    line_1 = Line2D([x0, x1], [y0, y1], linewidth=1,
                    linestyle="-", color="blue")
    line_2 = Line2D([x1, x2], [y1, y2], linewidth=1,
                    linestyle="-", color="cyan")
    line_3 = Line2D([x1, x3], [y1, y3], linewidth=1,
                    linestyle="--", color="cyan", alpha=0.4)

    ax.add_line(line_1)
    ax.add_line(line_2)
    ax.add_line(line_3)

    arc1 = Arc(
        [0, 0],
        plot_limit/10,
        plot_limit/10,
        0,
        0 if theta1 > 0 else degrees(theta1),
        degrees(theta1) if theta1 > 0 else 0,
        color="blue"
    )
    ax.add_patch(arc1)

    ax.text(
        plot_limit/10*cos(theta1/2),
        plot_limit / 15*sin(theta1/2),
        "%0.2f" % degrees(theta1)+u"\u00b0",
        fontsize=8,
        color="blue"
    )

    arc2 = Arc(
        [x1, y1],
        plot_limit/10,
        plot_limit/10,
        degrees(theta1),
        degrees(theta2) if theta2 < 0 else 0,
        0 if theta2 < 0 else degrees(theta2),
        color="cyan" if abs(degrees(theta2)) <= 135 else "red"
    )

    ax.text(
        x1 + plot_limit/10*cos(theta1 + theta2/2),
        y1 + plot_limit/10*sin(theta1 + theta2/2),
        "%0.2f" % degrees(theta2)+u"\u00b0",
        fontsize=8,
        color="cyan" if abs(degrees(theta2)) <= 135 else "red"
    )

    ax.add_patch(arc2)

    ax.text(
        x2 + plot_limit/25,
        y2 + plot_limit/25,
        "(" + "%0.2f" % px + "," + "%0.2f" % py + ")",
        fontsize=8,
        color="magenta"
    )

    ax.plot(px, py, 'o', color='m')
    ax.grid()

    plt.show()


def pruebasAleatorias(n):
    for i in range(n):
        l1 = random.random()
        l2 = random.random()
        px = 2*random.random()-1
        py = 2*random.random()-1

        print()
        print(f'Prueba {i}:')
        print(f'l1 = {l1}')
        print(f'l2 = {l2}')
        print(f'px = {px}')
        print(f'py = {py}')

        try:
            plotInverseK(l1, l2, px, py)
        except:
            print(
                f"No es posible alcanzar el punto ({px},{py}), con los brazos de longitud l1={l1} y l2={l2}")


def pruebasObtenerCoordenadas():
    while True:
        print()
        l1 = float(input('Ingrese la longitud del brazo 1: '))
        l2 = float(input('Ingrese la longitud del brazo 2: '))
        px = float(input('Ingrese la coordenada x del punto p: '))
        py = float(input('Ingrese la coordenada y del punto p: '))

        try:
            plotInverseK(l1, l2, px, py)
        except:
            print(
                f"No es posible alcanzar el punto ({px},{py}), con los brazos de longitud l1={l1} y l2={l2}")


if __name__ == '__main__':
    pruebasAleatorias(20)
    # pruebasObtenerCoordenadas()
