import matplotlib.pyplot as plt
import math
import numpy as np
from sympy import *


def plot_sums(x, y, col, fg):
    fg.fill_between(x, 0, y, color=col, alpha=0.33)


def plot_function(n, x, y, l, fg):
    fg.plot(x, y, label=l, color='black')
    fg.set_title(f'n = {n}')


def calculate_integral_sum(n, x, y, l, fg, xi_type):
    partitions = np.array_split(x, n)
    partitions_values = np.array_split(y, n)
    r = abs(partitions[0][0] - partitions[1][0])
    summ = 0
    for i in range(n):
        colour = "red"
        match xi_type:
            case "max_darbu":
                value = max(partitions_values[i])
                colour = "blue"
            case "min_darbu":
                value = min(partitions_values[i])
                colour = "green"
            case "левое":
                value = partitions_values[i][0]
            case "правое":
                value = partitions_values[i][-1]
            case "среднее":
                lenpart = len(partitions_values[i])
                value = partitions_values[i][lenpart//2]
            case _:
                value = np.random.choice(partitions_values[i])

        darbu = [value for x in range(len(partitions[i]))]
        plot_sums(partitions[i], darbu, colour, fg)
        summ += r * value
    plot_function(n, x, y, l, fg)
    return summ


def main():
    # для вычисления интегралов
    x, y, z = symbols('x y z')
    var = input("\nВведите свой вариант: ")
    # выбираем вариант
    match var:
        case "17":
            r = [-1, 1]
            x_range = np.arange(r[0], r[-1], 0.001)
            f = [x**2 for x in x_range]
            lab = "f(x) = x^2"
            intg = integrate(x**2, x)
            intg = lambdify(x, intg)
        case "21":
            r = [0, 2]
            x_range = np.arange(r[0], r[-1], 0.001)
            f = [4 ** x for x in x_range]
            lab = "f(x) = 4^x"
            intg = integrate(4 ** x, x)
            intg = lambdify(x, intg)
        case "28":
            r = [0, math.pi]
            x_range = np.arange(r[0], r[-1], 0.001)
            f = [math.cos(2*x) for x in x_range]
            lab = "f(x) = cos(2x)"
            intg = integrate(cos(2*x), x)
            intg = lambdify(x, intg)
        case _:
            main()
            return

    n = int(input("Введите кол-во точек разбиения: "))
    print("Оснащение: левое, правое, среднее, случайное")
    xi = input("Введите способ выбора оснащения: ")

    print("По формуле Лейбница:", intg(r[-1]) - intg(r[0]))
    fig, ax = plt.subplots(2)
    s1 = calculate_integral_sum(n, x_range, f, lab, ax[0], "max_darbu")
    s2 = calculate_integral_sum(n, x_range, f, lab, ax[0], "min_darbu")
    s3 = calculate_integral_sum(n, x_range, f, lab, ax[1], xi)
    print("Верхняя сумма Дарбу:", s1)
    print("Нижняя сумма Дарбу:", s2)
    print(f"Интегральная сумма (оснащение {xi}):", s3)

    plt.tight_layout()
    plt.show()
    main()
    return


main()

