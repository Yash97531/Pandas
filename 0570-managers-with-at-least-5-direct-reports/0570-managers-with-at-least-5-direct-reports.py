import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee
    a = df.groupby('managerId', dropna = False).size().reset_index(name = "count_id")
    b = df.merge(a, how = 'left', left_on='id', right_on='managerId').fillna({'count_id' : 0})
    c = b[b['count_id'] >= 5]
    return c[['name']]