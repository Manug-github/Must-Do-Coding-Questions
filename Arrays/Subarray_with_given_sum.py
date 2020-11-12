def subarray_with_given_sum(nums, k):
    """Program to find continous subarray which add to a given number, return index if found otherwise return -1 
    All elements of the array must not be negative
    Time Complexity O(n)
    Space Complexity O(1)
    """
    s = 0
    start = 0
    for i in range(len(nums)):
        s += nums[i]
        while s>k and start<len(nums) and start<i:
            s -= nums[start]
            start += 1
        if s==k:
            return [start, i]  
    return -1