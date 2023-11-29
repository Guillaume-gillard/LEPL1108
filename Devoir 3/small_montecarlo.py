import matplotlib.pyplot as plt
import numpy as np
import connect4

N = 100
win1_count = 0
win2_count = 0
draw_count = 0
win1_rate = []
win2_rate = []
draw_rate = []

for i in range(N):
    print("Simulation number: ", i + 1, " out of ", N)
    result = connect4.run_game()  # Run a game between AI student and AI random
    if result == 1:
        win1_count += 1
    elif result == 2:
        win2_count += 1
    else:
        draw_count += 1

    # Calculate and store win rates after each game
    win1_rate.append(win1_count / (i + 1))
    win2_rate.append(win2_count / (i + 1))
    draw_rate.append(draw_count / (i + 1))

# Calculate win rates
mean_win1_rate = np.mean(win1_rate)
mean_win2_rate = np.mean(win2_rate)
mean_draw_rate = np.mean(draw_rate)

# Plot win rates as points
plt.scatter(range(N), win1_rate, label='AI Student Win Rate')
plt.scatter(range(N), win2_rate, label='AI Random Win Rate')
plt.scatter(range(N), draw_rate, label='Draw Rate')

# Plot mean win rates as horizontal lines
plt.axhline(mean_win1_rate, color='blue', linestyle='--', label=f'Mean AI Student Win Rate: {mean_win1_rate:.2f}')
plt.axhline(mean_win2_rate, color='orange', linestyle='--', label=f'Mean AI Random Win Rate: {mean_win2_rate:.2f}')
plt.axhline(mean_draw_rate, color='green', linestyle='--', label=f'Mean Draw Rate: {mean_draw_rate:.2f}')

plt.xlabel('Number of Games')
plt.ylabel('Win Rate')
plt.legend()

# Add text annotations
plt.text(N + 1, mean_win1_rate, f'{mean_win1_rate:.2f}', color='blue')
plt.text(N + 1, mean_win2_rate, f'{mean_win2_rate:.2f}', color='orange')
plt.text(N + 1, mean_draw_rate, f'{mean_draw_rate:.2f}', color='green')

plt.show()
