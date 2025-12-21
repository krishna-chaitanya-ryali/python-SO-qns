"""
Problem:
--------
Implement a rate limiter that allows a client to make a maximum of
100 API requests per hour.

Approach:
---------
We use a Fixed Window Rate Limiting strategy:
- Track request count per client per hour window
- Reset count when the time window expires
"""

import time
from collections import defaultdict


class RateLimiter:
    """
    Fixed Window Rate Limiter implementation.
    """

    def __init__(self, max_requests: int, window_size_seconds: int):
        self.max_requests = max_requests
        self.window_size = window_size_seconds
        self.client_data = defaultdict(lambda: {"count": 0, "window_start": 0})

    def allow_request(self, client_id: str) -> bool:
        """
        Determines whether a request from a client is allowed.

        Args:
            client_id (str): Unique identifier for the client (IP / API key)

        Returns:
            bool: True if request is allowed, False otherwise.
        """
        current_time = int(time.time())
        client = self.client_data[client_id]

        # Initialize window
        if client["window_start"] == 0:
            client["window_start"] = current_time

        # Check if window has expired
        if current_time - client["window_start"] >= self.window_size:
            client["window_start"] = current_time
            client["count"] = 0

        # Check rate limit
        if client["count"] < self.max_requests:
            client["count"] += 1
            return True

        return False


if __name__ == "__main__":
    rate_limiter = RateLimiter(max_requests=100, window_size_seconds=3600)
    client_id = "client_123"

    # Simulate API requests
    for i in range(105):
        allowed = rate_limiter.allow_request(client_id)
        print(f"Request {i+1}: {'ALLOWED' if allowed else 'BLOCKED'}")


"""
This implementation uses a fixed time window approach.
For each client, we store the start time of the current window and the number of requests made.
If the client exceeds 100 requests within the same one-hour window, further requests are rejected.
Once the hour expires, the counter resets automatically.”
"""