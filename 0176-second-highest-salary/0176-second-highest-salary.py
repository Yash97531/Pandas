import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee
    a = df.drop_duplicates(subset = ["salary"], keep = 'first')
    if(len(a) < 2):
        import numpy as np
        return pd.DataFrame({'SecondHighestSalary' : [np.nan]})
    else:
        a.sort_values(by = 'salary', ascending = False, inplace = True)
        b = a['salary'].iloc[1]
        c = pd.DataFrame({'SecondHighestSalary' : [b]})
        return c