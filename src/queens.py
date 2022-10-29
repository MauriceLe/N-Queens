from random import randint, random
from numpy import unique


def init_population(size, queens):
    return [[randint(0,1) for x in range(queens)] for y in range(size)]


def decode(individual, bits):
    decoded = []
    
    for x in range(0, len(individual), bits):
        bit = ''
        
        for y in range(bits):
            bit += str(individual[x+y])
            
        decoded.append(int(bit, 2))
    
    return decoded


def fitness(individual):
    
    if individual == []:
        return 0
      
    queens = decode(individual, 3)
    score = 28
    score -= abs(len(queens) - len(unique(queens)))

    for x in range(len(queens)):  
        for y in range(x+1, len(queens)):
            if queens[y] == queens[x] + (x-y):
                score -= 1
            if queens[y] == queens[x] - (x-y):
                score -= 1
                
    return score


def fittest(population, fitness):
    best = []

    for individual in population:
        if fitness(individual) > fitness(best):
            best = individual

    return best


def selection(tournament, population):
    mating = []

    for x in range(len(population)):
        fittest = []

        for y in range(tournament):
            random = population[randint(0, len(population)-1)]
            
            if fitness(random) > fitness(fittest):
                fittest = random
            
        mating.append(fittest)
            
    return mating


def crossover(mating):
    probability = 0.6
    childs = []

    while len(childs) < len(mating):

        parent1 = mating[randint(0, len(mating)-1)]
        parent2 = mating[randint(0, len(mating)-1)]
    
        if random() < probability:
            index = randint(0, len(mating)-1)
            childs.append([*parent1[:index], *parent2[index:]])
            childs.append([*parent2[:index], *parent1[index:]])
        else:
            childs.append(parent1)
            childs.append(parent2)
    
    return childs


def mutation(population):
    probability = 0.01

    for individual in range(len(population)):
        for gene in range(len(population[individual])):
            if random() > probability:
                population[individual][gene] = 1 - population[individual][gene]
       
    return population


if __name__ == '__main__':

    maximum_runs = 100
    success_runs = 0

    generations = 100
    optimum = 28
    population = init_population(10, 8*3)

    for run in range(maximum_runs):

        for gen in range(generations):
            
            best = fittest(population, fitness)

            if fitness(best) == optimum:
                print(str(decode(best, 3)) + ' - Gen: ' + str(gen))
                success_runs += 1
                break

            mating = selection(3, population)
            childs = crossover(mating)
            pop = mutation(childs)
    
    print('Success-Rate: ' + (success_runs/maximum_runs*100))