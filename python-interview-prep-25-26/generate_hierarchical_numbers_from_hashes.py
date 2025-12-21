"""
Problem:
--------
Given a multiline string where each line contains one or more '#' characters,
generate hierarchical numbering based on the depth (number of '#').

Rules:
- Each '#' represents a level.
- Same level increments the last number.
- Deeper level starts with '.1'.
- Moving up resets deeper levels.

Example Input:
---------------
#
##
##
#
##
##
##
#
#

Example Output:
---------------
1
1.1
1.2
2
2.1
2.2
2.3
3
4
"""


def generate_hierarchy(input_text: str) -> list[str]:
    """
    Generates hierarchical numbering from hash-based input.

    Args:
        input_text (str): Multiline string containing '#' characters.

    Returns:
        list[str]: Hierarchical numbering output.
    """
    counters = []   # Keeps track of numbering at each level
    result = []

    for line in input_text.strip().splitlines():
        level = line.count("#")

        # If we go deeper, add new level starting at 1
        if level > len(counters):
            counters.append(1)

        # If we move up, truncate deeper levels
        else:
            counters = counters[:level]
            counters[-1] += 1

        # Build the hierarchical number string
        result.append(".".join(map(str, counters)))

    return result


if __name__ == "__main__":
    input_data = """
    #
    ##
    ##
    #
    ##
    ##
    ##
    #
    #
    """

    output = generate_hierarchy(input_data)

    print("Output:")
    for item in output:
        print(item)

"""
Expected Output:
----------------
1
1.1
1.2
2
2.1
2.2
2.3
3
4

Time Complexity:
----------------
O(n), where n is the number of lines.

Space Complexity:
-----------------
O(d), where d is the maximum depth of hierarchy.

I maintain a list that represents counters for each hierarchy level.
Each line’s number of # characters determines the level.
When going deeper, I append a new counter starting at 1.
When moving up, I truncate deeper levels and increment the current level.
This allows me to generate correct hierarchical numbering efficiently.”
"""
