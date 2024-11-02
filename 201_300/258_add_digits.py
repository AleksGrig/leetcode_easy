# 258. Add digits

# Given an integer num, repeatedly add all its digits until the result has only one digit, 
# and return it.


def addDigits(num):
    while num > 9:
        res = 0
        while num > 0:
            num, rest = divmod(num, 10)
            res += rest
        num = res
    return num


print(addDigits(38))