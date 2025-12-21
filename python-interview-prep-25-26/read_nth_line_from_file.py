"""
Problem:
--------
Write a function to read and return the Nth line from a text file.

If the file has fewer than N lines, return None.

This question tests:
- File handling
- Iteration with enumerate
- Edge case handling
"""


def get_nth_line(filename: str, n: int) -> str | None:
    """
    Returns the Nth line from a given file.

    Args:
        filename (str): Path to the text file.
        n (int): Line number to retrieve (1-based index).

    Returns:
        str | None: The Nth line content without newline character,
                    or None if file has fewer than N lines.
    """
    try:
        with open(filename, "r") as file:
            for index, line in enumerate(file, start=1):
                if index == n:
                    return line.strip("\n")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    return None


if __name__ == "__main__":
    file_name = "my_file.txt"
    line_number = 5

    result = get_nth_line(file_name, line_number)

    if result is not None:
        print(f"The {line_number}th line is: {result}")
    else:
        print(f'The file "{file_name}" does not have {line_number} lines.')

"""
Time Complexity:
----------------
O(n), where n is the line number requested.

Space Complexity:
-----------------
O(1), as the file is read line by line without loading it entirely into memory.
I open the file using a context manager and iterate line by line using enumerate.
When the index matches the required line number, I return the line.
This approach is memory efficient because it does not load the entire file.”
"""
