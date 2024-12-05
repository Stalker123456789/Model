import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Константа alpha
alpha = 0.1

def update(frame):
    plt.clf()  # Очистка текущего графика
    t = frame / 10  # Нормализация времени
    r = alpha * t  # Рассчитываем радиус
    phi = np.linspace(0, 2 * np.pi, 100) 
    x = r * np.cos(phi)  # Координаты x
    y = r * np.sin(phi)  # Координаты y
    plt.plot(x, y)  
    plt.xlim(-5, 5)  # Устанавливаем пределы по оси x
    plt.ylim(-5, 5)  # Устанавливаем пределы по оси y
    plt.gca().set_aspect('equal', adjustable='box')  # Сохраняем пропорции
    plt.title(f'Radius: {r:.2f}')  # Заголовок с радиусом

# Создаем фигуру
fig = plt.figure()

# Создаем анимацию
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

# Показываем анимацию
plt.show()
