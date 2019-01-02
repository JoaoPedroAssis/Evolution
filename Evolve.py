import os
import genome as gen

"""target = input('Inform the target: ')
pop_size = int(input('Inform the population size '))
mutation = float(input('Inform the mutation rate (in %): '))/100"""

# Parameters for the population and it's goal 
target ='PAO'
pop_size = 100
mutation = 0.01

population = gen.Population(pop_size, target, len(target), mutation)
arq = open('All_Phrases.txt', 'w')
arq.write('Genetic Algorithm -> Phrase Generator\n')
arq.close
while True:

    population.fitness()
    population.reproduction()

    os.system('clear')
    print("Best Specimen '{}'".format(population.best_one()))
    print('Generation {}'.format(population.generations))

    if population.got_to_target() == True:
        break




