# 367. Valid perfect square

# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer.
# In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.


def isPerfectSquare(num: int) -> bool:
    def search(left, right) -> bool:
        if left < right:
            middle = (left + right) // 2
            if middle**2 < num:
                return search(middle + 1, right)
            elif middle**2 > num:
                return search(left, middle - 1)
            else:
                return True
        elif left == right:
            return left**2 == num
        else:
            return False

    return search(1, num)


def isPerfectSquare2(num: int):
    left, right = 1, num
    while left <= right:
        middle = (left + right) // 2
        square = middle * middle
        if square == num:
            return True
        elif square < num:
            left = middle + 1
        else:
            right = middle -1
    return False


print(isPerfectSquare2(4))
