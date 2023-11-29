import numpy as np
import matplotlib.pyplot as plt
import connect4
import time
from concurrent.futures import ThreadPoolExecutor

t = time.time()

N = 10  # Number of repetitions
nb_games = [10, 100, 1000, 10000]
win1 = np.zeros((N, len(nb_games)))
draw = np.zeros((N, len(nb_games)))

def simulate_game(game_index):
    win1_count = 0
    draw_count = 0
    for j in range(nb_games[game_index]):
        print("Game number:", j + 1, "out of", nb_games[game_index])
        result = connect4.run_game()
        if result == 1:
            win1_count += 1
        elif result == 0:
            draw_count += 1
    return win1_count, draw_count

with ThreadPoolExecutor() as executor:
    # Simulate N times for each number of games using multithreading
    for i in range(N):
        print("Simulation number:", i + 1, "out of", N)
        for n in range(len(nb_games)):
            print("Number of games:", nb_games[n])
            # Use ThreadPoolExecutor to parallelize simulations
            results = executor.map(simulate_game, [n] * nb_games[n])
            win1_count, draw_count = zip(*results)
            win1[i][n] = np.sum(win1_count) / nb_games[n] * 100
            draw[i][n] = np.sum(draw_count) / nb_games[n] * 100

# Compute and print the mean for each [10, 100, 1000, 10000]
win1_mean = np.mean(win1, axis=0)
draw_mean = np.mean(draw, axis=0)
print(win1_mean)
print(draw_mean)

# Plot the results
plt.figure()
for i in range(len(nb_games)):
    plt.scatter(np.full(N, nb_games[i]), win1[:, i], c='blue', s=10)
    plt.scatter(np.full(N, nb_games[i]), draw[:, i], c='red', s=10)
    plt.scatter(nb_games[i], win1_mean[i], c='blue', marker='x', s=50)
    plt.scatter(nb_games[i], draw_mean[i], c='red', marker='x', s=50)

plt.legend(['Victoire joueur 1', 'Ex-aequo', 'Moyenne victoire joueur 1', 'Moyenne ex-aequo'])
plt.xlabel('Nombre de parties')
plt.ylabel('Probabilite en %')
plt.xscale("log")
plt.ylim((-10, 100))
plt.show()

elapsed = time.time() - t
print('Elapsed time:', elapsed)

plt.savefig('MCplot.png', format='png')
