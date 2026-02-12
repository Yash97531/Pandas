import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df = products
    a = df.melt(id_vars = 'product_id', var_name = 'store', value_name= "price")
    b = a.dropna(subset = ['price'])
    return b