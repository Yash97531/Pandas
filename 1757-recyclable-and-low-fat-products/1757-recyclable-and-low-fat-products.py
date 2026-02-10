import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products
    new = df[(df['low_fats'] == 'Y') & (df['recyclable'] == 'Y')]
    a = new.drop(columns = {"low_fats", 'recyclable'})
    return a