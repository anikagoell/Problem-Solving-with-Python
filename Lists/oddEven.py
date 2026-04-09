"""
Problem: Count Even and Odd Numbers

Given a list of integers, count how many numbers are even and how many are odd.

Example:
Input: [1, 2, 3, 4, 5]
Output: Even = 2, Odd = 3

Constraints:
- Do not use any built-in counting shortcuts
"""

def oddEven(arr):
    oddNumbers=0
    evenNumbers=0
    for i in arr:
        if i%2==0:
            evenNumbers+=1
        else:
            oddNumbers+=1
    return evenNumbers, oddNumbers

if __name__ == "__main__":
    try:
        arr=list(map(int,input("Enter elements: ").split()))
        even, odd = oddEven(arr)
        print(f"Even = {even}, Odd = {odd}")
    except ValueError:
        print("Please enter valid integers.")