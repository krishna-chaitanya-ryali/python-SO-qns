"""
Problem:
--------
Given two strings, return a list of unique common characters.
The output order must follow the order of appearance
in the SECOND input string.
# Case 1:
inputs:
    "pikachu", "togepi"
output:
    ["p", "i"]

# Case 2:
inputs:
    "arbitrary", "lemon"
output:
    []

# Case 3:
inputs:
    "testimonial", "ants"
output:
    ["a","n","t","s"]

# Case 4:
inputs:
    "ants", "testimonial"
output:
    ["t","s","n","a"]
"""

def get_common_chars_by_second_order(first: str, second: str) -> list[str]:
    """
    Returns unique common characters ordered by the second string.

    Args:
        first (str): First input string
        second (str): Second input string

    Returns:
        list[str]: Common characters ordered by second string
    """
    first_set = set(first)
    result = []
    seen = set()

    for char in second:
        if char in first_set and char not in seen:
            result.append(char)
            seen.add(char)

    return result


if __name__ == "__main__":
    test_cases = [
        ("pikachu", "togepi"),
        ("arbitrary", "lemon"),
        ("testimonial", "ants"),
        ("ants", "testimonial")
    ]

    for s1, s2 in test_cases:
        print(f"Input: {s1}, {s2}")
        print("Output:", get_common_chars_by_second_order(s1, s2))
        print("-" * 40)


"""
Input: pikachu, togepi
Output: ['p', 'i']

Input: arbitrary, lemon
Output: []

Input: testimonial, ants
Output: ['a', 'n', 't', 's']

Input: ants, testimonial
Output: ['t', 's', 'n', 'a']

"""