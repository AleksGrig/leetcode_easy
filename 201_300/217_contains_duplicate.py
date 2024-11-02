# 217. Contains duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.


def containsDuplicate1(nums):
    d = set()
    for num in nums:
        if num in d:
            return True
        d.add(num)    
    return False


def containsDuplicate2(nums):
    return len(nums) != len(set(nums))


l = [3, 4]
print(containsDuplicate1(l))
print(containsDuplicate2(l))