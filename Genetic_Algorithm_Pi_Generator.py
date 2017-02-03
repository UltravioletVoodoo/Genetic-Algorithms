#Program Name: Genetic_Algorithm_Pi_Generator.py
#Purpose: To generate Pi and learn about genetic algorithms
#Author: Jonathan Bezeau

import math
import random


def start():
	print "This program is currently undergoing maintenance"
	#1.	Create n randomized chromosomes
			#evaluate their fitness
			#rank them based on their fitness
	#2.	save the top 30% the rest die
	#3.	breed the surviving chromosomes until you have n chromosomes again
			#children have a chance to mutate
			#evaluate their fitness
			#rank them based on their fitness
	#4.	go to step 2
	
	
	#Step 1
	List = generate_initial_chromosomes()
	
	
	counter = 1
	while counter <= 100:
		#Step 2
		List = reduce_population(List)
		print List[0]
	
	
		#Step 3
		List = breed_survivors(List)
		
		
		
		print "Generation: %d"%counter
		counter = counter + 1
	
	List = reduce_population(List)
	print List[0]
	
	
	
	
	
	
	
def generate_initial_chromosomes():
	List = []
	counter = 0
	while counter < 100:
		List = List + [[float(random.randint(1000000000,5000000000))/1000000000, 0]]
		counter = counter + 1
	List = evaluate_fitness(List)
	List = fitness_rank(List)
	return List
	
def evaluate_fitness(List):
	for x in List:
		x[1] = (1 - abs(math.sin(x[0])))
	return List
	
def fitness_rank(List):
	List = sorted (List, key=lambda fitness: fitness[1])
	return List
	
def reduce_population(List):
	List2 = []
	counter = int(math.ceil(float(len(List))*0.3))
	counter2 = len(List)
	while counter > 0:
		List2 = List2 + [List[counter2 - 1]]
		counter2 = counter2 - 1
		counter = counter - 1
	counter = 0
	return List2
	
def breed_survivors(List):
	counter = 0
	while len(List) < 100:
		List = List + [make_child_chromosome(List[counter],List[counter + 1])]
	List = evaluate_fitness(List)
	List = fitness_rank(List)
	return List
	
def make_child_chromosome(Father, Mother):
	StrFather = str(Father[0])
	StrMother = str(Mother[0])
	child = []
	for x in StrFather:
		if x == ".":
			continue
		r = random.randint(1,2)
		if r == 1:
			chance = random.randint(1,10)
			if chance == 1:
				child = child + [str(random.randint(0,9))]
			else:
				child = child + [x]
		else:
			child = child + ["*"]
	length = len(child)
	while length > 0:
		if x == ".":
			continue
		if child[length - 1] == "*":
			chance = random.randint(1,10)
			if chance == 1:
				child[length - 1] = str(random.randint(0,9))
			else:
				child [length - 1] = StrMother[length - 1]
		length = length - 1
	child = float("".join(child))
	chance = random.randint(1,10)
	if chance == 1:
		secondChance = random.randint(1,2)
		if secondChance == 1:
			child = child + 0.1*child
		else:
			child = child - 0.1*child
	return [child, 0]
	
	
	
	
	
	
start()