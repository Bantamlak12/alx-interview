# 0x01-lockboxes

## Algorithm

- Create list variables named `opened_boxes` to isolate the opened boxes from the unopened ones, and `used_keys` to isolate the keys that are used to open a box (used keys from unused keys).
- Initialize the `opened_boxes` list with `boxes[0]`
- Iterate through the `opened_boxes` list. If there is an `IndexError` exception, handle it and continue the loop.
  - Iterate through the `keys` in the box. If there is an `IndexError` exception, handle it and continue the loop.
  - Check if the `key` is not one of the elements inside `used_keys`, then use the key to open the box and add the box to the `opened_boxes` list. Note: If the key is zero (0), don't add a box by that key because it's already there.
  - Finally, add the key to the `used_keys` list.
  - Repeat the loop.
- Repeat the loop.
- Check the length of `opened_boxes` if it's equal to the original `boxes` list. If it's return `True` else return `False`.

## Time and Space Complexity

The time and space complexity is `O(B + K)` where `B` is the total number of boxes and `K` is the total number of keys in the boxes.

- `opened_boxes` lists stores the boxes that are opened, In the worst case scenario, all boxes may need to be stored.

- Likewise, `used_keys` list stores the keys used to open the boxes, In the worst case, all keys may need to be stored.

So, both space and time complexity are linear with respect to the total number of boxes and keys.

## File

[0-lockboxes.py](./0-lockboxes.py)
