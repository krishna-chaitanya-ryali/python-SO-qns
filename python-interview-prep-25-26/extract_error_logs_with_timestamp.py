"""
Problem:
--------
Given a multiline log string, extract all ERROR messages along with
their corresponding timestamps.

Each log line follows this format:
YYYY-MM-DD HH:MM:SS LEVEL Message

We need to extract:
- ERROR message
- Time (HH:MM:SS)
"""

def extract_error_logs(log_data: str) -> list[str]:
    """
    Extracts ERROR messages and their timestamps from log data.

    Args:
        log_data (str): Multiline log string.

    Returns:
        list[str]: List of formatted error messages with timestamps.
    """
    error_logs = []

    for line in log_data.strip().splitlines():
        parts = line.split(maxsplit=3)

        # Expected format: date time level message
        if len(parts) == 4:
            date, time, level, message = parts
            if level == "ERROR":
                error_logs.append(f"{message} {time}")

    return error_logs


if __name__ == "__main__":
    log_string = """
    2025-10-06 10:15:22 INFO  Application started
    2025-10-06 10:16:05 ERROR Failed to connect to database
    2025-10-06 10:17:30 WARNING Low disk space
    2025-10-06 10:18:10 ERROR Unable to read config file
    """

    result = extract_error_logs(log_string)

    print("Output:")
    for entry in result:
        print(entry)

"""
Output:
-------
Failed to connect to database 10:16:05
Unable to read config file 10:18:10

Time Complexity:
----------------
O(n), where n is the number of log lines.

Space Complexity:
-----------------
O(k), where k is the number of ERROR log entries.

I split the log string into individual lines and then split each line into four parts using maxsplit=3.
This ensures that the message remains intact even if it contains spaces.
I filter only ERROR logs and extract the message along with the timestamp.
"""
