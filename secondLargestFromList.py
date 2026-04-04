def second_largest(arr):
    """
    Find the second largest element in a list.

    Args:
        arr (list): Input list of numbers

    Returns:
        int: The second largest number

    Raises:
        ValueError: If second largest does not exist
    """

    if len(arr) < 2:
        raise ValueError("List must have at least two elements")

    max1 = float('-inf')
    max2 = float('-inf')

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif max1 > num > max2:
            max2 = num

    if max2 == float('-inf'):
        raise ValueError("No second largest element found")

    return max2


if __name__ == "__main__":
    try:
        #n = int(input("Enter number of elements: "))
        arr = list(map(int, input("Enter elements: ").split()))
        print(f"The list is: {arr}")
        print(f"The second largest element is: {second_largest(arr)}")
    except ValueError as e:
        print(e)