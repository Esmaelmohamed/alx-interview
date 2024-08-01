#!/usr/bin/python3
"""
Module: lockboxes
Function: canUnlockAll

This module contains a function `canUnlockAll` which determines whether
all locked boxes can be opened starting from the first box, using keys 
that correspond to other boxes.
"""

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked starting from the first box.

    Args:
        boxes (list of lists): Each index i contains a list of keys that can 
                               unlock other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    n = len(boxes)
    reachable = {0}  # Start with box 0 (the first box)
    queue = [0]  # Initialize queue with box 0
    
    while queue:
        box_index = queue.pop(0)
        for key in boxes[box_index]:
            if 0 <= key < n and key not in reachable:
                reachable.add(key)
                queue.append(key)
    
    return len(reachable) == n

# Example usage:
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True
    
    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True
    
    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False

