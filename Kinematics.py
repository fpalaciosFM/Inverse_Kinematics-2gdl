from math import atan2, cos, sin,\
    pi, sqrt


class Kinematics:
    def __init__(self, length_1, length_2, thetalimit_1=pi, thetalimit_2=3.0*pi/4.0):
        self.length_1 = length_1
        self.length_2 = length_2
        self.thetalimit_1 = thetalimit_1
        self.thetalimit_2 = thetalimit_2

    def makeInverse(self, px, py):
        theta2 = self.makeTheta2(px, py)
        theta1 = self.makeTheta1(px, py, theta2)

        return (theta1, theta2)

    def makeTheta2(self, px, py):
        l1 = self.length_1
        l2 = self.length_2

        SinTheta2 = sqrt(1 - pow((px**2 + py**2 - l1**2 - l2**2)/(2*l1*l2), 2))
        CosTheta2 = (px**2 + py**2 - l1**2 - l2**2)/(2*l1*l2)

        SinTheta2 = SinTheta2 if px <= 0 else -SinTheta2

        return atan2(SinTheta2, CosTheta2)

    def makeTheta1(self, px, py, th2):
        l1 = self.length_1
        l2 = self.length_2

        SinTheta1 = sqrt(
            1 - pow((px*(l1+l2*cos(th2))+py*l2*sin(th2))/(px*px+py*py), 2))
        CosTheta1 = (px*(l1+l2*cos(th2))+py*l2*sin(th2))/(px*px+py*py)

        return atan2(SinTheta1, CosTheta1)


if __name__ == '__main__':
    pass
