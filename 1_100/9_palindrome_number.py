# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.


def isPalindrome(x):
    if x < 0:
        return False
    num = x
    res = 0
    
    while x:
        x, rest = divmod(x, 10)
        res = res * 10 + rest

    if num == res:
        return True
    else:
        return False
    

print(isPalindrome(121))