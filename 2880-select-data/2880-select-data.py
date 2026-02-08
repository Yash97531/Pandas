import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = students
    df = df[df["student_id"] == 101]
    df = df.drop(columns=["student_id"])
    return df

