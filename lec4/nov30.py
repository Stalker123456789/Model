import numpy as np
import matplotlib.pyplot as plt

def plot_ellipse(x_min, x_max, N, h=0, k=0, a=1, b=1):
    if N <= 0:
        raise ValueError("Количество точек N должно быть положительным.")
    if x_min >= x_max:
        raise ValueError("Неверные пределы: x_min должно быть меньше x_max.")

    x = np.linspace(x_min, x_max, N)
    y_positive = k + b * np.sqrt(1 - ((x - h) ** 2) / a ** 2)
    y_negative = k - b * np.sqrt(1 - ((x - h) ** 2) / a ** 2)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_positive, label='Верхняя половина эллипса', color='blue')
    plt.plot(x, y_negative, label='Нижняя половина эллипса', color='blue')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.title('График эллипса')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(x_min, x_max)
    plt.ylim(k - b - 1, k + b + 1)  
    plt.grid()
    plt.legend()
    plt.show()

plot_ellipse(2, 3, 1000, h=0, k=0, a=2, b=1)
