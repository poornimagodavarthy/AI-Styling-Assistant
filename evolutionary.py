import csv
import numpy as np
import pandas as pd

# Define weights for each attribute (higher weight means higher importance)
attribute_weights = {
    'gender': 1,
    'baseColour': 3,
    'season': 2,
    'usage': 2
}

# Define the population size
POPULATION_SIZE = 50

# Generate the initial population
def generate_population(user_preferences):
    population = []
    for _ in range(POPULATION_SIZE):
        individual = {
            'gender': np.random.choice(user_preferences['gender']),
            'baseColour': np.random.choice(user_preferences['baseColour']),
            'season': np.random.choice(user_preferences['season']),
            'usage': np.random.choice(user_preferences['usage'])
        }
        population.append(individual)
    return population

def crossover(parent1, parent2):
    # Implement crossover to generate offspring from parent individuals
    child = {}
    crossover_point = np.random.choice(list(parent1.keys()))
    for key in parent1:
        if key == crossover_point:
            child[key] = parent2[key]
        else:
            child[key] = parent1[key]
    return child

def mutation(individual, user_preferences):
    # Implement mutation to introduce diversity in the population
    mutated_individual = individual.copy()
    mutation_point = np.random.choice(list(user_preferences.keys()))
    mutated_individual[mutation_point] = np.random.choice(user_preferences[mutation_point])
    return mutated_individual

# The fitness function evaluates how close we are to the optimal solution
def evaluate_fitness(individual, user_preferences, attribute_weights):
    fitness = 0
    for key in user_preferences:
        if individual[key] in user_preferences[key]:
            fitness += attribute_weights.get(key, 0)
    return fitness

# Evolutionary algorithm
def evolutionary_algorithm(user_preferences, attribute_weights):
    best_individual = None
    best_fitness = 0
    population = generate_population(user_preferences)
    
    for generation in range(50):
        fitness_scores = [evaluate_fitness(individual, user_preferences, attribute_weights) for individual in population]

        for idx, fitness_score in enumerate(fitness_scores):
            if fitness_score > best_fitness:
                best_individual = population[idx]
                best_fitness = fitness_score

        # Generate new population through crossover and mutation
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = population[np.random.randint(0, POPULATION_SIZE)]
            parent2 = population[np.random.randint(0, POPULATION_SIZE)]
            child = crossover(parent1, parent2)
            if np.random.rand() < 0.2:  # 20% chance of mutation
                child = mutation(child, user_preferences)
            new_population.append(child)
        
        population = new_population

    return best_individual

def comparison(best_recommendation):
    # Comparing the best individual to every entry in the csv to find the best matches
    best_match_top = 0
    temp_count_top = 0
    best_id_top = None
    best_match_bot = 0
    temp_count_bot = 0
    best_id_bot = None

    df = pd.read_csv('styles.csv')
    for _, row in df.iterrows():
        temp_count_top = sum(1 for key in best_recommendation if row[key.lower()] == best_recommendation[key])
        temp_count_bot = sum(1 for key in best_recommendation if row[key.lower()] == best_recommendation[key])

        if row['subCategory'] == 'Topwear' and temp_count_top > best_match_top:
            best_match_top = temp_count_top
            best_id_top = row['id']
        
        if row['subCategory'] == 'Bottomwear' and temp_count_bot > best_match_bot:
            best_match_bot = temp_count_bot
            best_id_bot = row['id']

    return best_id_top, best_id_bot