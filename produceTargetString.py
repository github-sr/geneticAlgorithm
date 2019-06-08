# 	\ is line continuation character
# Given a target string, the goal is to produce target string starting from a random string of the same length. 
# In the following implementation, following analogies are made –
# 1. Characters A-Z, a-z, 0-9 and other special symbols are considered as genes
# 2. A string generated by these character is considered as chromosome/solution/Individual

# Fitness score is the number of characters which differ from characters in target string at a particular index.
# So individual having lower fitness value is given more preference.

import random 

# Number of individuals in each generation 
try:
	populationSize = int(input("Enter number of individuals in each generation: "))
except:
	populationSize = 101
if populationSize <= 0:
	populationSize = 101

# Valid genes 
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# Target string to be generated 
try:
	TARGET = input("Enter target string with length not less than 10: ")
except:
	TARGET = "Genetic algorithm using python"
if len(TARGET) < 10:
	TARGET = "Genetic algorithm using python"

class Individual(object): 
	''' 
	Class representing individual in population 
	'''
	def __init__(self, chromosome): 
		self.chromosome = chromosome 
		self.fitness = self.calFitness() 

	@classmethod
	def mutatedGenes(self): 
		''' 
		create random genes for mutation 
		'''
		global GENES 
		gene = random.choice(GENES) 
		return gene 

	@classmethod
	def createGnome(self): 
		''' 
		create chromosome or string of genes 
		'''
		global TARGET 
		gnomeLen = len(TARGET) 
		return [self.mutatedGenes() for _ in range(gnomeLen)] 

	def mate(self, par2): 
		''' 
		Perform mating and produce new offspring 
		'''

		# chromosome for offspring 
		childChromosome = [] 
		for gp1, gp2 in zip(self.chromosome, par2.chromosome):	 

			# random probability 
			prob = random.random() 

			# if prob is less than 0.45, insert gene 
			# from parent 1 
			if prob < 0.45: 
				childChromosome.append(gp1) 

			# if prob is between 0.45 and 0.90, insert 
			# gene from parent 2 
			elif prob < 0.90: 
				childChromosome.append(gp2) 

			# otherwise insert random gene(mutate), for maintaining diversity 
			else: 
				childChromosome.append(self.mutatedGenes()) 

		# create new Individual(offspring) using generated chromosome for offspring 
		return Individual(childChromosome) 

	def calFitness(self): 
		global TARGET 
		fitness = 0
		for gs, gt in zip(self.chromosome, TARGET): 
			if gs != gt: fitness+= 1
		return fitness 

# Driver code 
def main(): 
	global populationSize 

	#current generation 
	generation = 1

	found = False
	population = [] 

	# create initial population 
	for _ in range(populationSize): 
				gnome = Individual.createGnome() 
				population.append(Individual(gnome)) 
	
	while not found: 

		# sort the population in increasing order of fitness score 
		population = sorted(population, key = lambda x:x.fitness) 

		if population[0].fitness <= 0: 
			found = True
			break

		# Otherwise generate new offsprings for new generation 
		newGeneration = [] 

		# Perform Elitism, that mean 10% of fittest population 
		# goes to the next generation 
		s = int((10 * populationSize) / 100) 
		newGeneration.extend(population[:s]) 

		# From 50% of fittest population, Individuals 
		# will mate to produce offspring 
		s = int((90 * populationSize) / 100) 
		for _ in range(s): 
			parent1 = random.choice(population[:50]) 
			parent2 = random.choice(population[:50]) 
			child = parent1.mate(parent2) 
			newGeneration.append(child) 

		population = newGeneration 

		print("Generation: {} String: {} Fitness: {}".\
			format(generation, 
			"".join(population[0].chromosome), 
			population[0].fitness)) 

		generation += 1

# 	\ is line continuation character
	print("Generation: {} String: {} Fitness: {}".\
		format(generation, 
		"".join(population[0].chromosome), 
		population[0].fitness)) 

if __name__ == '__main__': 
	main() 
	input()