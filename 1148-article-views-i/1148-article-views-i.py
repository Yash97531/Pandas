import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views
    new = df[df['author_id'] == df['viewer_id']]
    a = new.sort_values(by = 'viewer_id', ascending = True)
    b = a.drop(columns = {'article_id', 'author_id', 'view_date'})
    c = b.drop_duplicates()
    return c.rename(columns = {'viewer_id' : 'id'})