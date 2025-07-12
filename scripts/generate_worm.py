# scripts/generate_worm.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import os

# Configuração da animação
fig, ax = plt.subplots(figsize=(8, 2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 2)
ax.axis('off')

# Desenha a minhoca como círculos
worm_body = [Circle((i, 1), 0.2, color='brown') for i in np.linspace(1, 9, 5)]
for segment in worm_body:
    ax.add_patch(segment)

# Animação
def update(frame):
    for i, segment in enumerate(worm_body):
        x_pos = i + frame * 0.1
        segment.center = (x_pos % 10, 1)
    return worm_body

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
ani.save('worm.gif', writer='pillow', fps=15)

print("Animação gerada: worm.gif")
