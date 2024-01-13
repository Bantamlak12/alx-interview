#!/usr/bin/python3
"""
File Name: 0-lockboxes.py

Function:
--------
canUnlockAll(boxes)
A module that determines if all the boxes can be opened.

"""


def canUnlockAll(boxes):
    """
    parameter:
    - boxes: A List of boxes that containes keys.

    Returns:
    - True if all boxes can be opened, else return False.
    """
    opened_boxes = [boxes[0]]
    used_keys = []

    for box in opened_boxes:
        try:
            for key in box:
                try:
                    if key not in used_keys:
                        if key != 0:
                            opened_boxes.append(boxes[key])
                        used_keys.append(key)
                except IndexError:
                    continue
        except IndexError:
            continue

    if len(opened_boxes) == len(boxes):
        return True
    else:
        return False
