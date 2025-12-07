import os

import pandas as pd
from pandas import DataFrame


def excel_column_remover(col):
    """
        Remove columns from file with data
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, "..", "data", "dataset.xlsx")
    path = os.path.abspath(path)

    df = pd.read_excel(path)

    df = df.drop(columns=[col])

    df.to_excel(path, index=False)

    return {"status": "success", "message": f"Column '{col}' removed and file saved."}


def excel_column_add(col):
    """
    Add columns in file with data
    """

    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, "..", "data", "dataset.xlsx")
    path = os.path.abspath(path)

    df = pd.read_excel(path)

    df['age'] = 'Unknown'

    df.to_excel(path, index=False)

    return {"status": "success", "message": f"Column '{col}' is added and file saved."}
