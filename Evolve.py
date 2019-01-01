#import numpy as np
import genome as gen

"""target = input('Inform the target: ')
pop_size = int(input('Inform the population size '))
mutation = float(input('Inform the mutation rate (in %): '))/100"""

# Parameters for the population and it's goal 
target = 'Joao Pedro'
pop_size = 100
mutation = 0.1

population = gen.Population(pop_size, target, len(target), mutation)

#population.fitness()
#population.probability()
cont = 0
while True:

    population.fitness()
    population.reproduction()

    print(population.best_one(), cont)

    if population.got_to_target() == True:
        break

    cont +=1



'''print(population.best_one())

population.reproduction()
population.fitness()

print(population.best_one())'''

