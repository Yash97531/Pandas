import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director
    a = df.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()
    b = a[a['timestamp'] >= 3]
    b.drop(columns = {'timestamp'}, inplace = True)
    return b