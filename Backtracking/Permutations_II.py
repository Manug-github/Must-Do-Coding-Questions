import itertools

def permutations_II_itertools(nums):    
    return [list(x) for x in set(itertools.permutations(nums))]

def permutations_II(nums):    
    pass