# 283. Move zeroes

# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


nums = [0, 0, 12, 3, 1]


def moveZeroes1(nums: list[int]):
    counter = 0
    try:
        while True:
            nums.remove(0)
            counter += 1
    except ValueError:
        for i in range(counter):
            nums.append(0)
    return nums


def moveZeroes2(nums: list[int]):
    counter = 0
    for num in nums:
        if num == 0:
            counter += 1

    for i in range(counter):
        nums.remove(0)

    for i in range(counter):
        nums.append(0)

    return nums


def moveZeroes3(nums: list[int]):
    for i in range(1, len(nums)):
        if nums[i] != 0:
            k = i
            while k > 0 and nums[k - 1] == 0:
                nums[k - 1], nums[k] = nums[k], nums[k - 1]
                k -= 1
    return nums


def moveZeroes4(nums: list[int]):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

print(moveZeroes4(nums))
