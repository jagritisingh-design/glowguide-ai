import pandas as pd

def clean_data(df):
    """
    Clean raw skincare dataset.
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df