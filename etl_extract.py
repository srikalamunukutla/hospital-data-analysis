import sqlite3
import pandas as pd

def extract_data():
    conn = sqlite3.connect('healthcare.db')
    query = "SELECT * FROM hospitals WHERE state = 'CA';"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

if __name__ == '__main__':
    df = extract_data()
    print(df.head())