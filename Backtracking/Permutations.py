import itertools

def permutations_itertools(nums):
    """Used itertools, valid to compare against backtracking algorithm"""
    return [list(x) for x in (itertools.permutations(nums))]

def permutations(nums):   
    pass 
    return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
