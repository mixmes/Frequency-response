
import math
import numpy as np
import matplotlib.pyplot as plt
import re

def get_coord_of_zeros_and_poles():
    coefs_of_zeros =  re.findall(r"-?\d+[\.\d+]*", input("Введите коэффициенты рекурсивной части (через пробел) > "))
    zeros = np.roots(coefs_of_zeros[::-1])
    zeros_coords = [[float(zeros[i].real),float(zeros[i].imag)] for i in range(len(zeros))]

    coefes_of_poles =  re.findall(r"-?\d+[\.\d+]*", input("Введите коэффициенты нерекурсивной части (через пробел) > "))
    poles = np.roots(coefes_of_poles[::-1])
    poles_coords = [[float(poles[i].real),float(poles[i].imag)] for i in range(len(poles))]
    draw_zeros_poles_plot(zeros_coords, poles_coords)
    return  zeros_coords,poles_coords

def draw_zeros_poles_plot(zeros_coord,poles_coord):
    [plt.plot(zeros_coord[i][0],zeros_coord[i][1],'o') for i in range(len(zeros_coord))]
    [plt.plot(poles_coord[i][0], poles_coord[i][1],'x') for i in range(len(poles_coord))]
    circle1 = plt.Circle((0, 0), 1, color='r', fill=False)
    ax = plt.gca()
    ax.add_patch(circle1)
    plt.axis('scaled')
    plt.xlabel("Real")
    plt.ylabel("Imagine")
    plt.savefig("/home/mihail/Рабочий стол/zeros-poles plot.png")
    plt.close();

def draw_afc_plot(afc_values):
    x_values = [i for i in range(361)]
    [plt.plot(x_values[i],afc_values[i],'.') for i in range(len(afc_values))]
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude-Frequency characteristic")
    plt.savefig("/home/mihail/Рабочий стол/Amplitude-Frequency characteristic.png")
    plt.close();


def frequency_response(N, P):
    circle_coords = []
    N_val = []
    P_val = []

    for i in range(361):
        x = math.cos(i * math.pi / 180)
        y = math.sin(i * math.pi / 180)
        circle_coords.append([x, y])

    for cc in circle_coords:
        b = []
        for el in N:
            b.append(math.sqrt((cc[0] - el[0]) ** 2 + (cc[1] - el[1]) ** 2))
        N_val.append(np.prod(b))

    for cc in circle_coords:
        b = []
        for el in P:
            b.append(math.sqrt((cc[0] - el[0]) ** 2 + (cc[1] - el[1]) ** 2))
        P_val.append(np.prod(b))

    res = [N_val[i] / P_val[i] for i in range(len(N_val))]

    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    coords = get_coord_of_zeros_and_poles()
    draw_afc_plot(frequency_response(coords[0],coords[1]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
