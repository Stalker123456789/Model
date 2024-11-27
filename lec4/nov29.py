import numpy as np
import matplotlib.pyplot as plt

def plot_hyperbola(x_min, x_max, N, k=1):
    if N <= 0:
        raise ValueError("Количество точек N должно быть положительным.")
    if x_min >= x_max:
        raise ValueError("Неверные пределы: x_min должно быть меньше x_max.")
    x = np.linspace(x_min, x_max, N)

    y_positive = k / x  
    y_negative = -k / x 
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_positive, label='Верхняя ветвь гиперболы', color='yellow')
    plt.plot(x, y_negative, label='Нижняя ветвь гиперболы', color='yellow')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.title('График гиперболы y = k/x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(x_min, x_max)
    plt.ylim(-10, 10)  
    plt.grid()
    plt.legend()
    plt.show()


plot_hyperbola(-10, 10, 1000, k=1)
