# N-Queens
> Solving the N-Queens problem using Genetic Algorithm

The aim of the N-Queens problem is to place N-Queens in such a manner on an NxN chessboard that no queens attack each other by being in the same row, column or diagonal.

![](header.png)

## Installation

```sh
pip install -r requirements.txt
```

## Terminology

- Individual: Coding of possible solutions
- Population: The set of all solutions
- Gene: An individual is characterized by a set of variables
- Fitness-Function: The fitness function assigns a value to a specific individual
- Selection: The selection selects possbile individuals for the later crossover
- Crossover: Also called recombination, is a genetic operator thats produces two offspring fromt two parents
- Mutation: It alters one or more gene values in a chromosome from its initial state

## Procedure

![](header.png)

- Step 1: Initilize start population
- Step 2: Check if the fitness optimum is reached with the current population 
- Step 3: If the optimum is not reached, select random individuals for the mating pool
- Step 4: Reproduce two random individuals from the mating pool
- Step 5: Mutate random genes from all individuals
- Step 6: Update the population with the new generation
- Repeat Step 2 to 6 until the optimum or maximum number of generations is reached
