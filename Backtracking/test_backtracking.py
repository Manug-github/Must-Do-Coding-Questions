from Permutations import permutations, permutations_itertools
from Permutations_II import permutations_II, permutations_II_itertools

def test_permutations():
    assert sorted(permutations_itertools([1,2,3])) == sorted(permutations_itertools([1,3,2]))


def test_permutations_II():
    assert sorted(permutations_itertools([1,2,3])) == sorted(permutations_II_itertools([1,3,2]))

