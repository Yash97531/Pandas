import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df = customers
    df.drop_duplicates("email", inplace = True)
    return df