import random
import string

class Population:
    def __init__ (self, pop_size, target_len):
        self.pop_size = pop_size
        self.target_len = target_len
        self.individuals = []

    def initialize_pop(self):
        for i in range(self.pop_size):
            self.individuals.append(''.join(random.choices(string.ascii_letters +
             ' ', k=self.target_len)))
             