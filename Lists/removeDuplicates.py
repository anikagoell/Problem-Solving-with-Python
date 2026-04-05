"""
Problem: Remove Duplicates from a List (Maintain Order)

Given a list of integers, remove duplicate elements while maintaining the original order.

Example:
Input: [1, 2, 2, 3, 4, 3]
Output: [1, 2, 3, 4]

Constraints:
- Do not use set() directly for final answer (because it does not maintain order).
"""

import __main__


def removeDuplicates(arr):
    newList=[]
    for i in arr:
        if i not in newList:
            newList.append(i)
    return newList

if __name__ == "__main__":
    try:
        arr=list(map(int,input("Enter elements: ").split()))
        print(f"The list after removing duplicates is: {removeDuplicates(arr)}")
    except ValueError:
        print("Please enter valid integers.")