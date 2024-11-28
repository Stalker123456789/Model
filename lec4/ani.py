import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

R = 1
t_max = -5 * np.pi  
frames = 150 
t_values = np.linspace(0, t_max, frames)

def update(frame):
    plt.clf()  
    t = t_values[frame]  
    
    x = R * (t - np.sin(t))  
    y = R * (1 - np.cos(t))  

    t_full = np.linspace(0, t, 100)  
    x_full = R * (t_full - np.sin(t_full))    
    y_full = R * (1 - np.cos(t_full))
    
    plt.plot(x_full, y_full, label='Циклоида', color='b')  
    plt.scatter(x, y, color='r')  
    plt.title('Анимация циклоида')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.xlim(-R * (t_max + 1), R * (t_max + 1)) 
    plt.ylim(-R * 3, R * 3)  
    plt.gca().set_aspect('equal', adjustable='box') 
    plt.legend()
