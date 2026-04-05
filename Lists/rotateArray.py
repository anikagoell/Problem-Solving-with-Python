"""
Problem: Rotate Array by k Steps

Given a list of integers, rotate the array to the right by k steps.

Example:
Input: [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

Constraints:
- Do it in-place if possible
"""

def rotateArray(arr, k):
    n = len(arr)
    k = k % n

    # Step 1: reverse whole array
    arr.reverse()

    # Step 2: reverse first k elements
    arr[:k] = reversed(arr[:k])

    # Step 3: reverse remaining elements
    arr[k:] = reversed(arr[k:])

    return arr

if __name__ == "__main__":
    try:
        arr=list(map(int,input("Enter elements: ").split()))
        k=int(input("Enter number of steps to rotate: "))
        print(f"The rotated array is: {rotateArray(arr, k)}")
    except ValueError:
        print("Please enter valid integers.")