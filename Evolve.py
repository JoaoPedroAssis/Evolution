#import numpy as np
import genome as gen

"""target = input('Inform the target: ')
pop_size = int(input('Inform the population size '))
mutation = float(input('Inform the mutation rate (in %): '))/100"""

# Parameters for the population and it's goal 
target = 'JohnPeter'
pop_size = 100
mutation = 0.01

population = gen.Population(pop_size, len(target))
population.initialize_pop()
print(population.individuals[1].fitness)