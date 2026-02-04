import pandas as pd

def run_query(query_statement, sql_connection):
    # Run the query on the database and print the output
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)