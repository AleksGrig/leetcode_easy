# 643. Maximum average subarray

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value
# and return this value. Any answer with a calculation error less than 10**-5 will be accepted.


nums = [1, 12, -5, -6, 50, 3]
k = 4


def findMaxAverage(nums: list[int], k: int):
    res = sum([nums[i] for i in range(0, k)])

    left = 0
    right = k
    while right < len(nums):
        new_sum = res - nums[left] + nums[right]
        if new_sum > res:
            res = new_sum
        left += 1
        right += 1
    return res / k


def findMaxAverage2(nums: list[int], k: int):
    res = sum(nums[:k])
    for i in range(len(nums) - k):
        res = max(res, res - nums[i] + nums[k + i])
    return res / k


print(findMaxAverage2(nums, k))
