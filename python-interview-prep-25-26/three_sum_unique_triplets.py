"""
Problem:
--------
Given an integer array nums, return all the unique triplets [nums[i], nums[j], nums[k]]
such that i != j != k and nums[i] + nums[j] + nums[k] == 0.

The solution must not contain duplicate triplets.

Example:
---------
Input:  [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
"""

from typing import List


def find_unique_triplets(nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in the array which sum to zero.

    Args:
        nums (List[int]): List of integers.

    Returns:
        List[List[int]]: List of unique triplets that sum to zero.
    """
    triplets = []
    n = len(nums)

    if n < 3:
        return triplets

    nums.sort()

    for i in range(n - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1   # ❗ FIXED (was incorrect in your code)

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for second and third elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    result = find_unique_triplets(nums)
    print("Output:")
    print(result)

"""
Output:
-------
[[-1, -1, 2], [-1, 0, 1]]

Time Complexity:
----------------
O(n^2)

Space Complexity:
-----------------
O(1)  (excluding output list)

I sort the array and fix one element at a time.
Then I use two pointers to find pairs whose sum equals the negative of the fixed element.
I skip duplicates at every step to ensure unique triplets.
This reduces the complexity from O(n³) to O(n²).”
"""
