"""
Problem:
--------
Find the maximum number in a list without using Python's built-in max() function.

This question tests:
- Looping logic
- Conditional checks
- Edge case handling
"""


def find_max_value(numbers: list[int]) -> int | None:
    """
    Finds the maximum value in a list of integers without using max().

    Args:
        numbers (list[int]): List of integers.

    Returns:
        int | None: Maximum value in the list, or None if the list is empty.
    """
    if not numbers:
        return None

    max_value = None

    for num in numbers:
        if max_value is None or num > max_value:
            max_value = num

    return max_value


if __name__ == "__main__":
    a = [50, 20, 30, 40, 10]

    result = find_max_value(a)

    print("Input List:", a)
    print("Maximum Value:", result)

"""
Output:
-------
Input List: [50, 20, 30, 40, 10]
Maximum Value: 50

Time Complexity:
----------------
O(n), where n is the number of elements in the list.

Space Complexity:
-----------------
O(1), constant extra space.

“I iterate through the list and keep track of the maximum value seen so far.
For each element, I compare it with the current maximum and update it if the element is larger.
This avoids using the built-in max() and works efficiently in linear time.”
"""
