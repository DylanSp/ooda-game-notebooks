from scipy import stats
from scipy.stats import randint
import numpy as np
import itertools

def dice_distribution(num_dice, min_roll, max_roll):
    single_dice_possible_rolls = np.arange(min_roll, max_roll + 1)
    roll_range = max_roll + 1 - min_roll
    single_dice_probabilities = [1 / roll_range] * roll_range
    single_dice_zipped = zip(single_dice_possible_rolls, single_dice_probabilities)
    
    # all possible combinations of dice rolls
    cartesian_product = list(itertools.product(single_dice_zipped, repeat = num_dice))

    possible_results = {}
    for possible_combination in cartesian_product:
        total = 0
        probability = 1
        for (roll_result, roll_probability) in possible_combination:
            total += roll_result
            probability *= roll_probability
            
        if total not in possible_results:
            possible_results[total] = 0
        possible_results[total] += probability
        
    all_dice_possible_rolls = []
    all_dice_probabilities = []
    for possible_roll, probability in possible_results.items():
        all_dice_possible_rolls.append(possible_roll)
        all_dice_probabilities.append(probability)
        
    return stats.rv_discrete(values=(all_dice_possible_rolls, all_dice_probabilities))

def probability_of_roll_geq_than_value(distro, value):
    return distro.sf(value - 1) # .sf() is survival function; returns chance of being > value, not >= value

distributions = {
    "1d4": dice_distribution(1, 1, 4),
    "2d4": dice_distribution(2, 1, 4),
    "1d6": dice_distribution(1, 1, 6),
    "2d6": dice_distribution(2, 1, 6)
}
