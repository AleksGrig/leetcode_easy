# 551. Student Attendance Record I

# You are given a string s representing an attendance record for a student 
# where each character signifies whether the student was absent, late, or present on that day. 
# The record only contains the following three characters:

#    'A': Absent.
#    'L': Late.
#    'P': Present.

# The student is eligible for an attendance award if they meet both of the following criteria:

#    The student was absent ('A') for strictly fewer than 2 days total.
#    The student was never late ('L') for 3 or more consecutive days.

# Return true if the student is eligible for an attendance award, or false otherwise.


s = "LALL"

def checkRecord(s: str):
    abs, late = 0, 0
    for cur in s:
        if cur == 'L':
            late += 1
            if late > 2:
                return False
        else:
            late = 0
            if cur == 'A':
                abs += 1
                if abs > 1:
                    return False
    return True


def checkRecord2(s: str):
    return s.count('A') < 2 and s.count('LLL') == 0 


print(checkRecord(s))