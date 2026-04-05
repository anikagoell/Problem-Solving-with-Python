"""
Problem: Find Missing Number

Given a list containing numbers from 1 to n with exactly one number missing, find the missing number.

Example:
Input: [1, 2, 4, 5]
Output: 3

Constraints:
- Numbers are from 1 to n
- Only one number is missing
"""

def missingNumber(ar):
    n=len(ar)+1
    expected_sum = n* (n+1) //2
    total_sum= sum(ar)
    return expected_sum - total_sum

if __name__ == "__main__":
    try:
        arr=list(map(int,input("Enter elements: ").split()))
        print(f"The missing number is: {missingNumber(arr)}")
    except ValueError:
        print("Please enter valid integers.")