import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales
    a = df.drop(columns = {'partner_id'})
    a.drop_duplicates(subset={'date_id', 'make_name', 'lead_id'}, inplace=True)
    a1 = a.groupby(['date_id', 'make_name'])['lead_id'].count().reset_index()
    b = df.drop(columns = {'lead_id'})
    b.drop_duplicates(subset={'date_id', 'make_name', 'partner_id'}, inplace=True)
    b1 = b.groupby(['date_id', 'make_name'])['partner_id'].count().reset_index()
    c = pd.merge(a1, b1, on = ['date_id', 'make_name'], how = "inner" )
    c.rename(columns = {'lead_id' : 'unique_leads', 'partner_id' : 'unique_partners'}, inplace=True)
    return c