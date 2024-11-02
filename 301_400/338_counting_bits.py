# 338. Counting bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.


def count_bits(n):
    solution = [0]

    for i in range(1, n+1):
        solution.append(solution[i//2] + i%2)

    return solution


def count_bits2(n):
    solution = [0]

    for i in range(1, n+1):
        cur = 0
        while i:
            cur += i & 1
            i >>= 1
        solution.append(cur)

    return solution

print(count_bits2(5))