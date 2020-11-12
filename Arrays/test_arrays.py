from Subarray_with_given_sum import subarray_with_given_sum
from Count_the_triplets import count_the_triplets

def test_subarray_with_given_sum():
    assert subarray_with_given_sum([1, 2, 3, 7, 5], 12) == [1, 3]
    assert subarray_with_given_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15) == [0,4]
    assert subarray_with_given_sum([1, 4, 20, 3, 10, 5], 33) == [2,4]
    assert subarray_with_given_sum([1, 4, 0, 0, 3, 10, 5], 7) == [1,4]
    assert subarray_with_given_sum([1, 4], 0) == -1

def test_count_the_triplets():
    assert count_the_triplets([1, 5, 3, 2]) == 2
    assert count_the_triplets([2, 3, 4]) == 0
    assert count_the_triplets([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 90
    assert count_the_triplets([10,2,1,2,4,6]) == 4