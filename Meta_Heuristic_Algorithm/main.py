#!/usr/bin/env python


from Meta_Heuristic_Algorithm.config import Config
from Meta_Heuristic_Algorithm.tools.dna import dna
from Meta_Heuristic_Algorithm.tools.draw_plot import show_plot
from Meta_Heuristic_Algorithm.tools.fitness import fitness
from Meta_Heuristic_Algorithm.tools.population import population
from Meta_Heuristic_Algorithm.tools.ranking import ranking
import streamlit as st

def geneticAlgorithm():
    """
    This function encapsulates the cappbilty of initializing chromosome population
    and then continue calculating fitness, generate ranking, perform crossover and
    mutation & repeating above steps until a defined stopping crietia is not met.
    """

    chr_population = population()

    chr_pop_fitness, chr_best_fitness_index = fitness(chr_pop=chr_population)

    chr_ranked_population = ranking(chr_pop_fitness=chr_pop_fitness, pop=chr_population)

    chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness,
        ranked_population=chr_ranked_population, chr_best_fitness_index=
        chr_best_fitness_index, last_pop=chr_population)

    show_plot(best_chromosome=chr_crossover_mutated_population[0])

    while not Config.stop_generation:

        prev_best_fit = chr_pop_fitness[chr_best_fitness_index[0], 0]

        chr_pop_fitness, chr_best_fitness_index = fitness(
            chr_pop=chr_crossover_mutated_population)

        chr_ranked_population = ranking(chr_pop_fitness=chr_pop_fitness, 
            pop=chr_crossover_mutated_population)

        chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness,
            ranked_population=chr_ranked_population, chr_best_fitness_index=
            chr_best_fitness_index, last_pop=chr_crossover_mutated_population)

        if prev_best_fit == chr_pop_fitness[chr_best_fitness_index[0], 0]:
            Config.stop_criteria += 1
        else:
            Config.stop_criteria = 0

        if Config.stop_criteria >= 5:
            Config.stop_generation = True

        geneticAlgoLogs = "Best chromosome is:" + str(chr_crossover_mutated_population[chr_best_fitness_index[0]]) 


        show_plot(best_chromosome=chr_crossover_mutated_population[0])
        Config.generations += 1
        st.write(geneticAlgoLogs)

    show_plot(best_chromosome=chr_crossover_mutated_population[0], inf_time=True)

