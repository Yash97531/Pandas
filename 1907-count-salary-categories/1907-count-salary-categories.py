import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    df = accounts
    a = df[df['income'] < 20000]
    b = df[(df['income'] >=20000) & (df['income']<= 50000) ]
    c = df[df['income'] > 50000]
    result = {'category': [ 'High Salary', 'Low Salary', 'Average Salary'],
    'accounts_count' : [ c.shape[0], a.shape[0], b.shape[0]]}
    x = pd.DataFrame(result)
    return x