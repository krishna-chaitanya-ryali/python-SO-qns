"""
Problem:
--------
Demonstrate how to safely update a shared variable in a multi-threaded
Python program using threading.Lock() to avoid race conditions.

This example shows:
- Global shared variable
- Lock acquisition and release
- Thread creation, start, and join
"""

import threading

# Shared resource
x = 0


def increment(lock: threading.Lock):
    """
    Safely increments the global variable x using a lock.

    Args:
        lock (threading.Lock): Lock object to synchronize access.
    """
    global x
    with lock:  # Automatically acquire and release lock
        x += 1


def thread_task(lock: threading.Lock, iterations: int):
    """
    Task executed by each thread.

    Args:
        lock (threading.Lock): Lock for synchronization.
        iterations (int): Number of times to increment x.
    """
    for _ in range(iterations):
        increment(lock)


def main():
    global x
    x = 0  # Reset shared variable

    lock = threading.Lock()
    iterations = 100000

    # Create threads
    t1 = threading.Thread(target=thread_task, args=(lock, iterations))
    t2 = threading.Thread(target=thread_task, args=(lock, iterations))

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to complete
    t1.join()
    t2.join()

    print("Final value of x:", x)


if __name__ == "__main__":
    main()

"""
Expected Output:
----------------
Final value of x: 200000

Time Complexity:
----------------
O(n), where n = total number of increments across threads.

Space Complexity:
-----------------
O(1), constant extra space.

Multiple threads increment a shared global variable.
Without a lock, this would cause a race condition.
I use threading.Lock() to ensure only one thread modifies the shared variable at a time.
The with lock: context manager guarantees safe acquisition and release of the lock.
"""
