# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


s = "abc"
t = "ahbgdc"


def isSubsequence(s, t):
    if len(s) > len(t):
        return False
    elif len(s) == 0:
        return True
    else:
        si, ti = 0, 0
        while ti < len(t):
            if t[ti] == s[si]:
                si += 1
                if si == len(s):
                    return True
            ti += 1
        return False


def isSubsequence1(s, t):
    stack = list(s)[::-1]
    for c in t:
        if stack and stack[-1] == c:
            stack.pop()
    return len(stack) == 0


def isSubsequence2(s, t):
    stack = list(s)
    for i in range(len(t)-1, -1, -1):
        if stack and stack[-1] == t[i]:
            stack.pop()
    return len(stack) == 0


def isSubsequence3(s, t):
    stack = list(s)
    for i in range(len(t)):
        if stack and stack[0] == t[i]:
            stack.pop(0)
    return len(stack) == 0

print(isSubsequence3(s, t))
