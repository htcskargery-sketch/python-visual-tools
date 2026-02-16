import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np

def generate_fibonacci_animation():
    n_squares = 10
    fibs = [1, 1]
    for _ in range(n_squares - 2):
        fibs.append(fibs[-1] + fibs[-2])
    
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#0e1117')
    ax.set_aspect('equal')
    ax.axis('off')

    origins = [(0, 0), (1, 0), (0, 1), (-2, 0), (-2, -5), (3, -5), (3, 3), (-18, 3), (-18, -31), (16, -31)]

    def update(frame):
        ax.clear()
        ax.axis('off')
        current_size = fibs[frame]
        margin = current_size * 0.5
        current_origins = origins[:frame+1]
        xs = [x for x, y in current_origins]
        ys = [y for x, y in current_origins]
        widths = fibs[:frame+1]
        min_x = min(x for x in xs); max_x = max(x + w for x, w in zip(xs, widths))
        min_y = min(y for y in ys); max_y = max(y + w for y, w in zip(ys, widths))
        ax.set_xlim(min_x - margin, max_x + margin); ax.set_ylim(min_y - margin, max_y + margin)
        for i in range(frame + 1):
            x, y = origins[i]; s = fibs[i]
            color = plt.cm.plasma(i / n_squares)
            rect = patches.Rectangle((x, y), s, s, linewidth=2, edgecolor='white', facecolor=color, alpha=0.8)
            ax.add_patch(rect)
            ax.text(x + s/2, y + s/2, str(s), color='white', ha='center', va='center', fontsize=12, fontweight='bold')

    ani = animation.FuncAnimation(fig, update, frames=len(origins), interval=800, repeat=True)
    ani.save('fibonacci_spiral.gif', writer='pillow', fps=2)

if __name__ == "__main__":
    generate_fibonacci_animation()
