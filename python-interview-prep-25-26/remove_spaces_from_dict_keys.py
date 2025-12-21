"""
Problem:
--------
Remove spaces from the keys of a Python dictionary using a lambda function.

This is a common Python interview question that tests:
- Dictionary comprehension
- Lambda functions
- String manipulation
"""

from typing import Dict


def remove_spaces_from_keys(data: Dict[str, str]) -> Dict[str, str]:
    """
    Removes spaces from all keys in the given dictionary.

    Args:
        data (Dict[str, str]): Input dictionary with string keys.

    Returns:
        Dict[str, str]: New dictionary with spaces removed from keys.

    Example:
        Input:
            {'first name': 'Krishna', 'last name': 'Chaitanya'}

        Output:
            {'firstname': 'Krishna', 'lastname': 'Chaitanya'}
    """
    # Lambda function with dictionary comprehension
    remove_spaces = lambda d: {key.replace(" ", ""): value for key, value in d.items()}
    return remove_spaces(data)


if __name__ == "__main__":
    # Sample input
    data = {
        'first name': 'Krishna',
        'last name': 'Chaitanya',
        'user role': 'Developer'
    }

    # Function call
    result = remove_spaces_from_keys(data)

    # Output
    print("Output:")
    print(result)

"""
Output:
-------
{'firstname': 'Krishna', 'lastname': 'Chaitanya', 'userrole': 'Developer'}

Time Complexity:
----------------
O(n), where n is the number of key-value pairs in the dictionary.

Space Complexity:
-----------------
O(n), since a new dictionary is created.

“I use a lambda function combined with dictionary comprehension.
For each key-value pair, I replace spaces in the key using str.replace() and construct a new dictionary.
This approach is clean, efficient, and does not mutate the original dictionary.”
"""
