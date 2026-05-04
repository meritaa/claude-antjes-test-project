import pandas as pd
from typing import Optional


def createDataFrame(rows: int = 5, columns: Optional[list] = None) -> pd.DataFrame:
    """
    Create a pandas DataFrame with specified rows and columns.

    Args:
        rows: Number of rows in the DataFrame (default: 5).
        columns: List of column names. If None, uses ['col1', 'col2', 'col3'].

    Returns:
        A pandas DataFrame with the specified structure and sample data.
    """
    if columns is None:
        columns = ['col1', 'col2', 'col3']

    data = {col: range(rows) for col in columns}
    return pd.DataFrame(data)


if __name__ == '__main__':
    df = createDataFrame()
    print(df)
