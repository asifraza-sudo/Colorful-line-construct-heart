import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


root = tk.Tk()
root.title("Colorful Heart with Name Animation")


fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')


t = np.linspace(0, 2 * np.pi, 500)  
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)


text = ax.text(0, 0, '', ha='center', va='center', fontsize=20, color='white')


colors = plt.cm.rainbow(np.linspace(0, 1, len(t)))


def update(frame):
    ax.clear()
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.axis('off')
    
    for i in range(frame):
        ax.plot(x[:i], y[:i], color=colors[i])
    
    text.set_text('Harish')
    text.set_position((0, -18 + frame * 0.1))
    ax.add_artist(text)


ani = animation.FuncAnimation(fig, update, frames=len(t), interval=5, repeat=False) 


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


root.mainloop()
