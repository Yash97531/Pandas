import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    df['bonus'] = df['salary']
    df.loc[df['employee_id']%2 == 0, 'bonus'] = 0
    df.loc[df['name'].str[0] == "M", 'bonus'] = 0
    df.sort_values(by = 'employee_id', ascending = True, inplace = True)
    a = df.drop(columns = {'name', 'salary'})
    return a