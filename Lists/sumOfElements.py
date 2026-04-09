"""
Problem: Sum of Elements in a List

Given a list of integers, find the sum of all elements.

Example:
Input: [1, 2, 3, 4]
Output: 10

Constraints:
- Do not use built-in sum()
"""

def sumOfElements(arr):
    total=0
    for i in arr:
        total+=i
    return total

if __name__ == "__main__":
    try:
        