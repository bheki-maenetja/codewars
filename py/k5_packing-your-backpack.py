# Description

# You're about to go on a trip around the world! On this trip you're bringing your trusted backpack, that anything fits into. The bad news is that the airline has informed you, that your luggage cannot exceed a certain amount of weight.

# To make sure you're bringing your most valuable items on this journey you've decided to give all your items a score that represents how valuable this item is to you. It's your job to pack you bag so that you get the most value out of the items that you decide to bring.

# Your input will consist of two arrays, one for the scores and one for the weights. You input will always be valid lists of equal length, so you don't have to worry about verifying your input.

# You'll also be given a maximum weight. This is the weight that your backpack cannot exceed.

# For instance, given these inputs:

# scores = [15, 10, 9, 5]
# weights = [1, 5, 3, 4]
# capacity = 8
# The maximum score will be 29. This number comes from bringing items 1, 3 and 4.

# Note: Your solution will have to be efficient as the running time of your algorithm will be put to a test.

# SOLUTION
from random import sample
from itertools import combinations

def pack_bagpack(scores, weights, capacity):
    weight_set = list(set(weights))
    weight_dict = {}.fromkeys(weight_set, [])
    weights_and_scores = list(zip(weights, scores))
    weight_combos = []
    for weight in weight_set:
      score_tups = [i[1] for i in weights_and_scores if i[0] == weight]
      weight_dict[weight] = score_tups
    print(weight_dict)
    # print(weights_and_scores)
    for i in range(1, len(weights) + 1):
        new_combos = [combo for combo in list(combinations(weights, i)) if sum(combo) <= capacity]
        # print(new_combos)
        weight_combos += new_combos
    print(weight_combos)
    score_totals = [ sum([max(weight_dict[i]) for i in combo]) for combo in weight_combos]
    # print(score_totals)
    return max(score_totals)

scores = [17, 5, 9, 13, 10, 12, 4, 11, 2, 14, 8, 14, 15, 3, 16, 2, 1, 17, 9, 18, 20, 16]
weights = [3, 4, 2, 3, 3, 4, 1, 2, 3, 5, 3, 3, 2, 5, 1, 1, 3, 3, 1, 4, 4, 2]
capacity = 161

print(pack_bagpack(scores, weights, capacity))