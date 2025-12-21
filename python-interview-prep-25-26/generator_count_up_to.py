"""
Problem:
--------
Create a generator function that yields numbers from 1 up to a given maximum value.

This question tests:
- Understanding of generators
- Usage of `yield`
- Memory-efficient iteration
"""


def count_up_to(max_value: int):
    """
    Generator that yields numbers from 1 up to max_value (inclusive).

    Args:
        max_value (int): The maximum number to yield.

    Yields:
        int: Next number in sequence.

    Example:
        Input:
            max_value = 5

        Output:
            1 2 3 4 5
    """
    current = 1
    while current <= max_value:
        yield current
        current += 1


if __name__ == "__main__":
    counter = count_up_to(5)

    print("Output:")
    for number in counter:
        print(number)

"""
Output:
-------
1
2
3
4
5

Time Complexity:
----------------
O(n), where n is max_value.

Space Complexity:
-----------------
O(1), since generators yield values one at a time without storing the full sequence.

This function is a generator because it uses the yield keyword.
Instead of returning all values at once, it produces values one at a time, which is memory efficient.
Generators are useful when working with large datasets or streams of data.
"""
