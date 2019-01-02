import random
import string
from difflib import SequenceMatcher

class Specimen:
    def __init__(self, len):
        # Generates random string with the same length of the target 
        self.phrase = ''.join(random.choices(string.ascii_letters +
         ' ', k=len))
        # Initialize the fitness and probability 
        self.fitness = -1
        self.probability = 0
    
    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def calculate_fitness(self, target):
        
        # Calculates the number of correct letters in
        # a given position
        score = 0
        for i in range(len(target)):
            if self.phrase[i] == target[i]:
                score += 1
        # Raises to fourth power so a little step in the
        # score means a big step in the fitness
        self.fitness = score**4

    def register(self, arq):
        arq.write(self.phrase + '\n')

class Population:
    def __init__ (self, pop_size, target, target_len, mutation):
        self.pop_size = pop_size
        self.target_len = target_len
        self.target = target
        self.mutation = mutation
        self.individuals = []
        # Function to initialize the first population
        for i in range(self.pop_size):
            # Create an individual
            individual = Specimen(self.target_len)
            # Append the individuals to the population
            self.individuals.append(individual)
        
        self.generations = 1

    def fitness(self):
        # Evaluate the fitness of the entire population
        arq = open('All_Phrases.txt', 'a')
        arq.write('\n---------- Generation {} ----------\n'.format(self.generations))
        for individual in self.individuals:
            individual.calculate_fitness(self.target)
            individual.register(arq)

        arq.close()
        self.probability()
        

    def probability(self):
        # Calculate the probability of a specimen being
        # picked for mating
        count = 0
        for individual in self.individuals:
            count += individual.fitness

        for individual in self.individuals:
            individual.probability = individual.fitness/count
        
    def pick_one(self):
        # Pick one specimen based on it's probability of being picked
        index = 0 
        rand = random.uniform(0,1)

        while rand > 0:
            rand = rand - self.individuals[index].probability
            index += 1

        index -= 1
        return self.individuals[index].phrase

    def reproduction(self):
        # For each individual, select two parents and mate them
        for individual in self.individuals:
            father = self.pick_one()
            mother = self.pick_one()
            child = crossing_over(father, mother, self.target)
            # Mutate the child according to the mutation rate
            new_child = self.mutate(child)
            individual.phrase = new_child

        self.generations += 1

    def best_one(self):
        # Returns the best specimen of the population
        max_index = self.individuals.index(max(self.individuals))
        return self.individuals[max_index].phrase

    '''def got_to_target(self):
        # Checks if the best 
        best_one = self.best_one()
        if best_one == self.target:
            return True
        else:
            return False'''

    def mutate(self, child):
        # According to the mutation rate, randomly
        # switch a character
        for char in child:
            if random.uniform(0,1) < self.mutation:
                child = child.replace(char, random.choice(string.ascii_letters + ' '), 1)
        return child

def crossing_over(father, mother, target):
    # Gets the half of the fathers genes and combine
    # with half of the mothers
    length = int(len(father)/2)    
    return father[:length] + mother[length:]
