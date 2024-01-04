# 0x00. Pascal's Triangle

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

As it can be seen above, `Pascal's triangle` is a pattern where each element in a row is the sum of the two elements directly above it.

### Algorithm

- Take the number of rows to be printed, denoted as `n`.
- Initialize `triangle` as `[[1]]`, representing the first row.
- Make the outer iteration `i` from `0` to `n - 1`. For each iteration a new row will be created.
- Store the previous row in a variable `temp`. It adds `0` at both ends to facilitate the sum of adjacent elements in the previous row.
- Initialize an empty list `row` to store the elements of the current row.
- Make inner iteration from `0` to a length of the previous row plus one. Length of a previous row is `len(triangle[-1]) + 1` or `len(temp) - 1`
- Add the previous adjacent row elements and append them to the `row` variable. i.e `temp[j] + temp[j + 1]`
- Append the row to the triangle list
- Continue the outer loop until `n` rows are created in the triangle.
- Finally, return the triangle

## Time and Space Complexity

- O(n^2)

## File

[0-pascal_triangle.py](./0-pascal_triangle.py)
