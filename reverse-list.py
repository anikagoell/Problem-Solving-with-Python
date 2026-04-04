def reverse_list(arr):
    """
    Reverse a list in-place.

    Args:
        arr (list): Input list

    Returns:
        list: Reversed list
    """
    left, right = 0, len(arr) - 1  # Initialize two pointers, one at the start and one at the end of the list

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4, 5]))
    print(reverse_list([22,56,43,67,89,90]))
    print(reverse_list(['a', 'b', 'c', 'd', 'e']))