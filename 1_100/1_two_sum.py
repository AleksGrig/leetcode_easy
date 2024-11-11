# 1. Two sum

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.


nums = [3, 3, 3, 4]
target = 7
d = {}


def solution1():
    for index, num in enumerate(nums):
        target_index = d.get(target - num)
        if d.get(num) == None:
            d[num] = index
        if target_index != None:
            return (index, target_index) if index < target_index else (target_index, index)


def solution2():
    for index1, num1 in enumerate(nums):
        for index2, num2 in enumerate(nums):
            if index1 != index2 and num1 + num2 == target:
                return (index1, index2)


print(solution1())
print(solution2())
