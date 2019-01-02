import os
import genome as gen

# Parameters for the population and it's goal 
target ='Eu quero lolo'
pop_size = 100
mutation = 0.01

# Writing the header of the file that will contain all generated phrases
arq = open('All_Phrases.txt', 'w')
arq.write('Genetic Algorithm -> Phrase Generator\n')
arq.close

# Initializing the population
population = gen.Population(pop_size, target, len(target), mutation)

while True:

    # Evaluating the fitness of the entire population
    population.fitness()
    # Reproducing specimens and getting the next generation
    population.reproduction()

    os.system('clear')
    print("Best Specimen '{}'".format(population.best_one()))
    print('Generation {}'.format(population.generations))

    if population.best_one() == target:
        break




