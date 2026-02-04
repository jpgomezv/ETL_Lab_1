import sqlite3

def load_to_csv(df, target_file):
    # Save the dataframe to a CSV file without the index
    df.to_csv(target_file, index=False)

def load_to_db(df, sql_connection, table_name):
    # Save the dataframe to the SQLite database
    # if_exists='replace' means it will overwrite the table if it already exists
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)