import matplotlib.pyplot as plt
import math
import numpy as np

n = 10  # частей равномерного разбиения

# выбираем вариант
var = "17"  # ! заменить на input()
match var:
    case "17":
        curr_range = [-1, 1]
        x_range = np.arange(-1, 1, 0.001)
        f = [x**2 + 5*x for x in x_range]
        lab = "f(x) = x^2"
    case _:
        curr_range = []
        x_range = []
        f = []
        lab = ""

norm = (curr_range[-1] - curr_range[0]) / n  # мелкость разбиения
intervals = []
# разбиваем интервал
partitions = np.array_split(x_range, n)
partitions_values = np.array_split(f, n)
for i in range(n):
    # верхняя сумма Дарбу
    max_value = max(partitions_values[i])
    darbu = [max_value for x in range(len(partitions[i]))]
    if i == 0:
        plt.fill_between(partitions[i], 0, darbu, color='gray', alpha=0.5, label="Верхняя сумма Дарбу")
    else:
        plt.fill_between(partitions[i], 0, darbu, color='gray', alpha=0.5)
    # нижняя сумма Дарбу
    min_value = min(partitions_values[i])
    darbu = [min_value for x in range(len(partitions[i]))]
    if i == 0:
        plt.fill_between(partitions[i], 0, darbu, color='green', alpha=0.5, label="Нижняя сумма Дарбу")
    else:
        plt.fill_between(partitions[i], 0, darbu, color='green', alpha=0.5)

plt.plot(x_range, f, label=lab, color='black')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График формулы, суммы Дарбу')

plt.legend()
plt.show()