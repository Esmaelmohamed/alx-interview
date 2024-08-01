#!/usr/bin/python3
"""
Module: lockboxes
Function: canUnlockAll

This module contains a function `canUnlockAll` which determines whether
all locked boxes can be opened starting from the first box, using keys 
that correspond to other boxes.

Usage:
>>> boxes = [[1], [2], [3], [0]]
>>> canUnlockAll(boxes)
True
"""

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked starting from the first box.

    Args:
    - boxes (list of lists): Each index i contains a list of keys that can 
      unlock other boxes.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    reachable = set([0])  # Start with box 0 (the first box)
    
    for box_index in reachable:
        for key in boxes[box_index]:
            if key < len(boxes) and key not in reachable:
                reachable.add(key)
    
    return len(reachable) == len(boxes)

# Example usage:
if __name__ == "__main__":
    boxes = [[1], [2], [3], [0]]
    print(canUnlockAll(boxes))

