"""
Problem:
--------
Given a Pandas DataFrame, select the row with the maximum value of column 'B'
for each group in column 'A'.

This question tests:
- Pandas groupby
- idxmax usage
- Row selection based on aggregated values
"""

import pandas as pd


def get_max_rows_per_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns rows that have the maximum value of column 'B' for each group in column 'A'.

    Args:
        df (pd.DataFrame): Input DataFrame with columns A, B, C.

    Returns:
        pd.DataFrame: DataFrame containing rows with max B per A.
    """
    return df.loc[df.groupby("A")["B"].idxmax()]


if __name__ == "__main__":
    # Sample input data
    data = pd.DataFrame({
        "A": [1, 1, 2, 2],
        "B": [10, 20, 10, 30],
        "C": [100, 200, 300, 400]
    })

    result = get_max_rows_per_group(data)

    print("Input DataFrame:")
    print(data)
    print("\nOutput DataFrame:")
    print(result)

"""
Output:
-------
   A   B    C
1  1  20  200
3  2  30  400

Time Complexity:
----------------
O(n), where n is the number of rows in the DataFrame.

Space Complexity:
-----------------
O(1) extra space (excluding output DataFrame).
I group the DataFrame by column A and use idxmax() on column B to get the index of the row with the maximum value in each group.
Then I use .loc[] to select those rows from the original DataFrame

Alternative Solution
df.sort_values("B", ascending=False).drop_duplicates("A")
"""
