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
        self.probability = 0
    
    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def calculate_fitness(self, target):
        #self.fitness = (int((SequenceMatcher(None, self.phrase, target).ratio())*100))**2
        score = 0
        for i in range(len(target)):
            if self.phrase[i] == target[i]:
                score += 1
        self.fitness = score**3

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

    def fitness(self):
        # Evaluate the fitness of the entire population
        for individual in self.individuals:
            individual.calculate_fitness(self.target)

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

        self.probability()

        for individual in self.individuals:
            father = self.pick_one()
            mother = self.pick_one()
            child = crossing_over(father, mother)
            '''if self.mutation > random.uniform(0,1):
                #print('passou')
                rand = random.randint(0, len(self.target))
                letter = random.choice(string.ascii_letters)
                # print(rand)
                child.replace(individual.phrase[rand-1], letter, 1)'''

            individual.phrase = child
        
        self.mutate()

    def best_one(self):
        
        max_index = self.individuals.index(max(self.individuals))
        return self.individuals[max_index].phrase, self.individuals[max_index].fitness

    def got_to_target(self):

        best_one,_ = self.best_one()
        if best_one == self.target:
            return True
        else:
            return False
    def mutate(self):

        mut = int(100*self.mutation)
        for i in range(mut):
            chosen = random.choice(self.individuals)
            rand = random.randint(1,self.target_len)
            letter = random.choice(string.ascii_letters + ' ')
            chosen.phrase = chosen.phrase.replace(chosen.phrase[rand-1], letter, 1)

def crossing_over(father, mother):
    
    length = int(len(father)/2)    
    return father[:length] + mother[length:]

