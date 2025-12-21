"""
Problem:
--------
Given a string containing alphabets and digits, find the sum of all numbers
present in the string.

Numbers may be multi-digit and appear anywhere in the string.
"""

def sum_numbers_in_string(input_string: str) -> int:
    """
    Calculates the sum of all numeric values present in a string.

    Args:
        input_string (str): Input string containing characters and digits.

    Returns:
        int: Sum of all numbers found in the string.

    Example:
        Input:
            "te123s26t11"

        Output:
            160  (123 + 26 + 11)
    """
    current_number = ""
    total_sum = 0

    for char in input_string:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                total_sum += int(current_number)
                current_number = ""  # Reset for next number

    # Handle case where string ends with a number
    if current_number:
        total_sum += int(current_number)

    return total_sum


if __name__ == "__main__":
    s = "te123s26t11"
    result = sum_numbers_in_string(s)

    print("Input:", s)
    print("Output:", result)

"""
Output:
-------
Input: te123s26t11
Output: 160

Time Complexity:
----------------
O(n), where n is the length of the string.

Space Complexity:
-----------------
O(n) in the worst case for storing digits of a number.

“I iterate through the string character by character.
When I encounter digits, I build the number as a string.
When a non-digit is found, I convert the collected digits to an integer and add it to the total.
Finally, I handle the edge case where the string ends with digits.”
"""
