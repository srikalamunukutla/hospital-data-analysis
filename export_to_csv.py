import sqlite3
import pandas as pd

def export_to_csv():
    conn = sqlite3.connect('healthcare.db')
    df = pd.read_sql_query("SELECT * FROM hospitals", conn)
    conn.close()

    # Save to CSV
    df.to_csv("hospital_data_export.csv", index=False)
    
if __name__ == '__main__':
    export_to_csv()