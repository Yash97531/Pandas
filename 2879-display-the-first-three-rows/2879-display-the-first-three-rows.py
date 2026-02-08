import pandas as pd

def selectFirstRows(employees):
    df = pd.DataFrame(employees)
    a = df.head(3)
    return a

print(selectFirstRows)