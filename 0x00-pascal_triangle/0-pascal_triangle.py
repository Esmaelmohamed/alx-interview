#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        List[List[int]]: A list of lists representing Pascal's Triangle. 
                         Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]
    
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        previous_row = triangle[i - 1]
        
        # Compute the values in between the 1s
        for j in range(len(previous_row) - 1):
            row.append(previous_row[j] + previous_row[j + 1])
        
        # End each row with a 1
        row.append(1)
        # Add the newly computed row to the triangle
        triangle.append(row)
    
    return triangle
