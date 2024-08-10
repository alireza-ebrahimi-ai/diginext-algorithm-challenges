def search_matrix(matrix, target):
    """
    Searches for a target value in a 2D matrix with the following properties:
    - The numbers in each row are sorted in ascending order from left to right.
    - The first number of each row is greater than the last number of the previous row.
    
    This function uses a binary search approach to efficiently find the target value.

    :param matrix: List[List[int]], the 2D matrix to search in.
    :param target: int, the value to search for.
    :return: bool, True if the target is found, False otherwise.
    """
    
    # Edge case: if the matrix is empty or has no columns, return False
    if not matrix or not matrix[0]:
        return False

    # Dimensions of the matrix
    m, n = len(matrix), len(matrix[0])

    # Initialize the binary search range
    left, right = 0, m * n - 1

    # Perform binary search on the 'flattened' matrix
    while left <= right:
        # Find the middle index of the current search range
        mid = (left + right) // 2
        
        # Convert the 1D index back to 2D indices
        mid_value = matrix[mid // n][mid % n]

        # Check if the middle element is the target
        if mid_value == target:
            return True
        # If the target is greater, ignore the left half
        elif mid_value < target:
            left = mid + 1
        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    # If we exit the loop, the target was not found
    return False

# Example usage:
matrix = [[1, 3, 5], [7, 8, 10], [12, 15, 18]]
target = 8
print(search_matrix(matrix, target))  # Output: True
