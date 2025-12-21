"""
Problem:
--------
Given a dictionary with mixed value types, create a new dictionary
containing only numeric values (int or float), where:
- Original values become keys
- Original keys become values

This question tests:
- Dictionary comprehension
- Type checking using isinstance()
"""

from typing import Dict, Any


def extract_numeric_values(data: Dict[str, Any]) -> Dict[float, str]:
    """
    Extracts numeric values from a dictionary and reverses key-value pairs.

    Args:
        data (Dict[str, Any]): Input dictionary with mixed value types.

    Returns:
        Dict[float, str]: Dictionary with numeric values as keys and original keys as values.

    Example:
        Input:
            {'Name': 'A', 'Age': 30, 'Weight': 70, 'Height': 5.2, 'Hobby': 'Reading'}

        Output:
            {30: 'Age', 70: 'Weight', 5.2: 'Height'}
    """
    return {
        value: key
        for key, value in data.items()
        if isinstance(value, (int, float))
    }


if __name__ == "__main__":
    data = {
        'Name': 'A',
        'Age': 30,
        'Weight': 70,
        'Height': 5.2,
        'Hobby': 'Reading'
    }

    result = extract_numeric_values(data)

    print("Input Dictionary:")
    print(data)
    print("\nOutput Dictionary:")
    print(result)

"""
Output:
-------
{30: 'Age', 70: 'Weight', 5.2: 'Height'}

Time Complexity:
----------------
O(n), where n is the number of items in the dictionary.

Space Complexity:
-----------------
O(k), where k is the number of numeric values extracted.

I iterate over the dictionary using .items() and use isinstance() to filter numeric values.
Then I construct a new dictionary by reversing the key-value pairs using dictionary comprehension.
This approach is concise, readable, and efficient.
"""
