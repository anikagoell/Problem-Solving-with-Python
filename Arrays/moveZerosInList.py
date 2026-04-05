def moveZeros(arr):
    ''' Move all zeros in a list to the end while maintaining the order of non-zero elements.
        Args:
            arr (list): Input list of numbers
        Returns:
            list: List with zeros moved to the end
    '''
    # Initialize a pointer for the position of the next non-zero element
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr
if __name__== "__main__":
    try:
        input_list=list(map(int,input("Enter the list elements separated by space: ").split()))
        print(f"The entered list is: {input_list}")
        print(f"The list with zeros moved to the end is: {moveZeros(input_list)}")
    except ValueError:
        print("Please enter valid integers.")