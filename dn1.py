import random
import numpy as np
from numpy import sqrt, dot, cross
from numpy.linalg import norm

import matplotlib.pyplot as plt
import matplotlib.animation as anim


class Receiver:

    def __init__(self):
        self.x = random.uniform(25, 75)
        self.y = random.uniform(25, 75)
        self.z = random.uniform(25, 75)


class Satelite:

    def __init__(self):
        self.x = random.uniform(0, 100)
        self.y = random.uniform(0, 100)
        self.z = random.uniform(0, 100)
        self.point = np.array([self.x, self.y, self.z])

    def distance(self, receiver: Receiver) -> float:
        return ((self.x - receiver.x)**2 + (self.y - receiver.y)**2 + (self.z - receiver.z)**2)**(1/2)


# Find the intersection of three spheres
# P1,P2,P3 are the centers, r1,r2,r3 are the radii
# Implementaton based on Wikipedia Trilateration article.
def trilaterate(P1, P2, P3, r1, r2, r3):
    temp1 = P2-P1
    e_x = temp1/norm(temp1)
    temp2 = P3-P1
    i = dot(e_x, temp2)
    temp3 = temp2 - i*e_x
    e_y = temp3/norm(temp3)
    e_z = cross(e_x, e_y)
    d = norm(P2-P1)
    j = dot(e_y, temp2)
    x = (r1*r1 - r2*r2 + d*d) / (2*d)
    y = (r1*r1 - r3*r3 - 2*i*x + i*i + j*j) / (2*j)
    temp4 = r1*r1 - x*x - y*y
    if temp4 < 0:
        raise Exception("The three spheres do not intersect!")
    z = sqrt(temp4)
    p_12_a = P1 + x*e_x + y*e_y + z*e_z
    p_12_b = P1 + x*e_x + y*e_y - z*e_z
    return p_12_a, p_12_b


class Drawer:

    def __init__(self):
        self.satelites = [Satelite() for i in range(3)]
        self.receiver = Receiver()
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        self.receiver_plt, = ax.plot([], [], [], marker="o",
                                     markersize=20, markerfacecolor="lightcoral", markeredgecolor="lightcoral")

        self.satelite_lines = []

        for satelite in self.satelites:
            ax.plot(satelite.x, satelite.y, satelite.z, marker="o",
                    markersize=20, markerfacecolor="grey", markeredgecolor="grey")
            self.satelite_lines.append(ax.plot([], [], [], marker="o",
                                      markersize=10, markerfacecolor="red", markeredgecolor="red")[0])
            

        self.intersect1_plt, = ax.plot([], [], [], marker="o",
                                      markersize=10, markerfacecolor="blue", markeredgecolor="blue")

        self.intersect2_plt, = ax.plot([], [], [], marker="o",
                                      markersize=10, markerfacecolor="blue", markeredgecolor="blue")
        
        self.receiver_txt = ax.text(self.receiver.x, self.receiver.y ,self.receiver.z, "")


        self.animation = anim.FuncAnimation(
            fig, self.update, interval=20, blit=True, save_count=50)
        plt.show()

    def calculate_position(self):
        return trilaterate(self.satelites[0].point, self.satelites[1].point,
                           self.satelites[2].point,
                           self.satelites[0].distance(self.receiver),
                           self.satelites[1].distance(self.receiver),
                           self.satelites[2].distance(self.receiver))

    def update(self, i):
        self.receiver.x += .1
        self.receiver_plt.set_data([self.receiver.x], [self.receiver.y])
        self.receiver_plt.set_3d_properties([self.receiver.z])

        # self.receiver_txt.set_data([self.receiver.x], [self.receiver.y])
        # self.receiver_txt.set_3d_properties([self.receiver.z])
        # self.receiver_txt.set_text(f"XD")

        # if i % 10 == 0:
        intersect1, intersect2 = self.calculate_position()
        self.intersect1_plt.set_data([intersect1[0]], [intersect1[1]])
        self.intersect1_plt.set_3d_properties([intersect1[2]])
        self.intersect2_plt.set_data([intersect2[0]], [intersect2[1]])
        self.intersect2_plt.set_3d_properties([intersect2[2]])

        for i, satelite_line in enumerate(self.satelite_lines):
            satelite_line.set_data([self.satelites[i].x, self.receiver.x], [self.satelites[i].y, self.receiver.y])
            satelite_line.set_3d_properties([self.satelites[i].z, self.receiver.z])



        return self.receiver_plt, self.intersect1_plt, self.intersect2_plt, self.receiver_txt

# drawer = Drawer()

# def update():
#     draw


Drawer()
