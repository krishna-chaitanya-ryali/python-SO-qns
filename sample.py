#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module docstring: A brief description of the script's purpose.
"""

import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def my_function(input_data):
    """
    Function docstring: Describes what the function does.

    Args:
        input_data: Description of the input data.

    Returns:
        Description of the return value.
    """
    try:
        # Function logic
        result = input_data * 2
        return result
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    logging.info("Script started")

    # Get input data
    try:
        input_value = int(input("Enter a number: "))
    except ValueError:
        logging.error("Invalid input. Please enter a number.")
        sys.exit(1)

    # Call the function
    output_value = my_function(input_value)

    if output_value is not None:
        print(f"The result is: {output_value}")
    else:
        logging.warning("No result generated")

    logging.info("Script finished")