import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(person, address, on='personId', how='left').loc[:,['firstName', 'lastName', 'city', 'state']]
