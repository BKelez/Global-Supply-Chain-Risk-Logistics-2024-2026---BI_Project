from data_access import query_to_dataframe
from query_loader import load_query


query = load_query("lead_time_by_transport")

df = query_to_dataframe(query)

print(df)