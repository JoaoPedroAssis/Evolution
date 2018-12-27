import random
import string

class Specimen:
    def __init__(self, len):
        # Generates random string with the same length of the target 
        self.phrase = ''.join(random.choices(string.ascii_letters +
         ' ', k=len))
        # Initialize the fitness
        self.fitness = -1
    

class Population:
    def __init__ (self, pop_size, target_len):
        self.pop_size = pop_size
        self.target_len = target_len
        self.individuals = []

    def initialize_pop(self):
        # Function to initialize the first population
        for i in range(self.pop_size):
            # Create an individual
            individual = Specimen(self.target_len)
            # Append the individuals to the population
            self.individuals.append(individual)


