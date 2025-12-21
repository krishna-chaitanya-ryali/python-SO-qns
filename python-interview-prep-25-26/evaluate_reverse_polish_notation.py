"""
Problem:
--------
Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).

Valid operators are +, -, *, and /.
Each operand may be an integer or another expression.

Note:
- Division should truncate toward zero.

Examples:
---------
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: (2 + 1) * 3 = 9

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: 4 + (13 / 5) = 6
"""


def evaluate_rpn(tokens: list[str]) -> int:
    """
    Evaluates a Reverse Polish Notation expression.

    Args:
        tokens (list[str]): List of tokens representing RPN expression.

    Returns:
        int: Evaluated result.
    """
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Truncate division toward zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]


if __name__ == "__main__":
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
    ]

    for tokens, expected in test_cases:
        result = evaluate_rpn(tokens)
        print(f"Input: {tokens}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print("-" * 40)

"""
Time Complexity:
----------------
O(n), where n is the number of tokens.

Space Complexity:
-----------------
O(n) for the stack.

Reverse Polish Notation can be efficiently evaluated using a stack.
When I encounter a number, I push it onto the stack.
When I encounter an operator, I pop the top two operands, apply the operation, and push the result back.
At the end, the stack contains a single value — the result.High_Level_Solution_Architecture.md

"""
