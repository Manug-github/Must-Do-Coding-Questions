def count_the_triplets(nums):
    """Program to count how many combinations of three numbers such that sum of two makes the third element in array
    Time Complexity O(n^2), Sort in Python is O(nlogn)
    Space Complexity O(n), The sort method sorts a list in place, it does use some additional space. https://en.wikipedia.org/wiki/Timsort
    """
    nums.sort()
    i = len(nums)-1
    ans = 0
    while i>=0:
        j = 0
        k = i-1
        while j<k:
            if nums[j] + nums[k] == nums[i]:
                ans += 1
                j += 1
            elif nums[j] + nums[k] > nums[i]:
                k -= 1
            else:
                j += 1
        i -=1
    return ans
