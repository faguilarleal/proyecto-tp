##PROBLEMA RESOLVIENDOLO UTILIZANDO LEY DE LOS GRANDES NÚMEROS
print("PROBLEMA RESOLVIENDOLO UTILIZANDO LEY DE LOS GRANDES NÚMEROS")
import random

def simulate_game():
    sequence = []
    while True:
        flip = random.choice(['C', 'X'])
        sequence.append(flip)

        if len(sequence) >= 3:
            last_three = ''.join(sequence[-3:])
            if last_three == 'CCC':
                return 'Menganita'
            elif last_three == 'XCX':
                return 'Chispudito'

def simulate_games(num_games):
    results = {'Menganita': 0, 'Chispudito': 0}
    for _ in range(num_games):
        winner = simulate_game()
        results[winner] += 1

    prob_menganita = results['Menganita'] / num_games
    prob_chispudito = results['Chispudito'] / num_games

    return prob_menganita, prob_chispudito

num_games = 100000
prob_menganita, prob_chispudito = simulate_games(num_games)
print(f"Probabilidad de que gane Menganita: {prob_menganita}")
print(f"Probabilidad de que gane Chispudito: {prob_chispudito}")