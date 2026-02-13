import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders
    a = df.groupby('customer_number', as_index = False)['order_number'].count()
    a.sort_values(by = "order_number", ascending = False, inplace = True)
    b = a.head(1)
    b.drop(columns = {'order_number'}, inplace = True)
    
    return b