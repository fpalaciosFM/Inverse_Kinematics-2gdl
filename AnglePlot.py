import math
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Arc

def get_angle_plot(line1, line2, offset=1, color=None, origin=[0, 0], len_x_axis=1, len_y_axis=1):

    l1xy = line1.get_xydata()

    # Angle between line1 and x-axis
    slope1 = (l1xy[1][1] - l1xy[0][1]) / float(l1xy[1][0] - l1xy[0][0])
    # Taking only the positive angle
    angle1 = abs(math.degrees(math.atan(slope1)))

    l2xy = line2.get_xydata()

    # Angle between line2 and x-axis
    slope2 = (l2xy[1][1] - l2xy[0][1]) / float(l2xy[1][0] - l2xy[0][0])
    angle2 = abs(math.degrees(math.atan(slope2)))

    theta1 = min(angle1, angle2)
    theta2 = max(angle1, angle2)

    angle = theta2 - theta1

    if color is None:
        # Uses the color of line 1 if color parameter is not passed.
        color = line1.get_color()

    return Arc(origin, len_x_axis*offset, len_y_axis*offset, 0, theta1, theta2, color=color, label=str(angle)+u"\u00b0")


def get_angle_text(angle_plot):
    angle = angle_plot.get_label()[:-1]  # Excluding the degree symbol
    angle = "%0.2f" % float(angle)+u"\u00b0"
    return angle


if __name__ == '__main__':
    pass
