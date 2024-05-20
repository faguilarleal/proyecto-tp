##PROBLEMA RESOLVIENDOLO UTILIZANDO LEY DE LOS GRANDES NÚMEROS
print("PROBLEMA RESOLVIENDOLO UTILIZANDO LEY DE LOS GRANDES NÚMEROS")
import random

def simulate_game(num_flips):
    sequence = []
    results = {'Menganita': 0, 'Chispudito': 0}
    
    for _ in range(num_flips):
        flip = random.choice(['C', 'X'])
        sequence.append(flip)
        sequence = sequence[-3:]
        
        if sequence == ['C', 'C', 'C']:
            results['Menganita'] += 1
        elif sequence == ['X', 'C', 'X']:
            results['Chispudito'] += 1

    return results


num_games = 100000
simulation_results = simulate_game(num_games)
total_games = simulation_results['Chispudito']+simulation_results['Menganita']
print(simulation_results['Chispudito'])
print(simulation_results['Menganita'])
print(total_games)
prob_menganita = simulation_results['Menganita'] / total_games
prob_chispudito = simulation_results['Chispudito'] / total_games
print(f"Probabilidad de que gane Menganita: {prob_menganita}")
print(f"Probabilidad de que gane Chispudito: {prob_chispudito}")