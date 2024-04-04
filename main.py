import matplotlib.pyplot as plt
import math
import numpy as np
from sympy import *


def plot_sums(x, y, col, fg):
    fg.fill_between(x, 0, y, color=col, alpha=0.33)


def plot_function(n, x, y, lab, fg):
    fg.plot(x, y, label=lab, color='black')
    fg.set_title(f'n = {n}')


def calculate_integral_sum(n, x, y, lab, fg, xi_type):
    partitions = np.array_split(x, n)
    partitions_values = np.array_split(y, n)
    r = abs(partitions[0][0] - partitions[1][0])
    summ = 0
    for i in range(n):
        colour = "red"
        valuel = max(partitions_values[i])
        valuer = min(partitions_values[i])
        if i != 0:
            valuel = partitions_values[i-1][-1]
        if i != n-1:
            valuer = partitions_values[i+1][0]
        match xi_type:
            case "max_darbu":
                value = max(partitions_values[i])
                value = max(valuel, value, valuer)
                colour = "blue"
            case "min_darbu":
                value = min(partitions_values[i])
                value = min(valuel, value, valuer)
                colour = "green"
            case "левое":
                value = partitions_values[i][0]
            case "правое":
                value = partitions_values[i][-1]
            case "среднее":
                lenpart = len(partitions_values[i])
                value = partitions_values[i][lenpart // 2]
            case _:
                value = np.random.choice(partitions_values[i])
        darbu = [value for x in range(len(partitions[i]))]
        plot_sums(partitions[i], darbu, colour, fg)
        summ += r * value
    plot_function(n, x, y, lab, fg)
    return round(summ, 3)


def main():
    var = input("\nВведите свой вариант: ")
    x = symbols('x')  # для integrate
    # выбираем вариант
    match var:
        case "9":
            lab = "f(x) = x^2"
            r = [-3, 0]
            x_range = np.arange(r[0], r[-1], 0.001)
            f = [x ** 2 for x in x_range]
            intg = integrate(x ** 2, x)
            intg = lambdify(x, intg)  # первообразные
        case "17":
            lab = "f(x) = x^2"
            r = [-1, 1]
            x_range = np.arange(r[0], r[-1], 0.001)
            f = [x ** 2 for x in x_range]
            intg = integrate(x ** 2, x)
            intg = lambdify(x, intg)  # первообразные
        case "21":
            lab = "f(x) = 4^x"
            r = [0, 2]
            x_range = np.arange(r[0], r[-1], 0.001)
            f = [4 ** x for x in x_range]
            intg = integrate(4 ** x, x)
            intg = lambdify(x, intg)
        case "28":
            lab = "f(x) = cos(2x)"
            r = [0, math.pi]
            x_range = np.arange(r[0], r[-1], 0.001)
            f = [math.cos(2 * x) for x in x_range]
            intg = integrate(cos(2 * x), x)
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
