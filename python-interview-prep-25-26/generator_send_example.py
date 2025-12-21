"""
Problem:
--------
Demonstrate two-way communication with a Python generator using `yield` and `send()`.

This example shows how:
- A generator can receive values from the caller
- Maintain internal state
- Process input dynamically
"""


def interactive_generator():
    """
    A generator that receives values using send() and processes them.

    Yields:
        str: Status or processed output based on input sent.
    """
    value = yield "initialized"

    while True:
        if value is not None:
            print(f"Generator received: {value}")
            value = yield f"processed: {value.upper()}"
        else:
            value = yield "waiting for input"


if __name__ == "__main__":
    g = interactive_generator()

    # Start the generator
    print(next(g))  # Initializes the generator

    # Send values to the generator
    print(g.send("start"))
    print(g.send("continue"))
    print(g.send("end"))

"""
Output:
-------
initialized
Generator received: start
processed: START
Generator received: continue
processed: CONTINUE
Generator received: end
processed: END

Time Complexity:
----------------
O(n) where n is the number of send() operations.

Space Complexity:
-----------------
O(1), generator maintains constant state.

This generator demonstrates two-way communication.
The first next() call initializes the generator and reaches the first yield.
After that, values are sent using send(), which assigns the sent value to the variable on the left of yield.
The generator processes the input and yields a response back to the caller.”
"""
