"""
Problem: Find Maximum and Minimum in a List

Given a list of integers, find the maximum and minimum elements without using built-in functions like max() and min().

Example:
Input: [3, 5, 1, 8, 2]
Output: Max = 8, Min = 1

Constraints:
- The list will contain at least one element.
- Do not use built-in functions like max() or min().
"""

def maximum(arr):
    maximum_element = arr[0]
    for num in arr:
        if num> maximum_element :
            maximum_element = num
    return maximum_element

def minimum(arr):
    minimum_element = arr[0]
    for num in arr:
        if num < minimum_element:
            minimum_element = num
    return minimum_element

if __name__ == "__main__":
    try:
        input_list = list(map(int, input("Enter the list elements separated by space: ").split()))
        print(f"The entered list is: {input_list}")
        print(f"The maximum element is: {maximum(input_list)}")
        print(f"The minimum element is: {minimum(input_list)}")
    except ValueError:
        print("Please enter valid integers.")