import random
import string
from difflib import SequenceMatcher

class Specimen:
    def __init__(self, len):
        # Generates random string with the same length of the target 
        self.phrase = ''.join(random.choices(string.ascii_letters +
         ' ', k=len))
        # Initialize the fitness 
        self.fitness = -1
    
    def calculate_fitness(self, target):
        self.fitness = SequenceMatcher(None, self.phrase, target).ratio()
    

class Population:
    def __init__ (self, pop_size, target, target_len):
        self.pop_size = pop_size
        self.target_len = target_len
        self.target = target
        self.individuals = []

    def initialize_pop(self):
        # Function to initialize the first population
        for i in range(self.pop_size):
            # Create an individual
            individual = Specimen(self.target_len)
            # Append the individuals to the population
            self.individuals.append(individual)

    def pop_fitness(self):

        for individual in self.individuals:
            individual.calculate_fitness(self.target) 
