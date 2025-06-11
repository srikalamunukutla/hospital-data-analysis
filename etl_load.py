import pandas as pd
import sqlite3

def load_and_clean_data(csv_file):
    df = pd.read_csv(csv_file)

    df.rename(columns={
        'Facility ID': 'provider_id',
        'Facility Name': 'hospital_name',
        'Emergency Services': 'emergency_services'
    }, inplace=True)

    df = df.dropna(subset=['provider_id', 'hospital_name'])

    df['emergency_services'] = df['emergency_services'].fillna('Unknown')

    #df['provider_id'] = df['provider_id'].astype(str).str.strip()
    
    return df

def insert_data_to_db(df):
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()

    for _, row in df.iterrows():
        provider_id = str(row['provider_id']).strip()
        if not provider_id:
            continue
        cursor.execute('SELECT COUNT(*) FROM hospitals WHERE provider_id = ?', (provider_id,))
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO hospitals (
                    provider_id, hospital_name, address, city, state, zip_code, phone_number, hospital_type, emergency_services
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                provider_id,
                row.get('hospital_name', ''),
                row.get('Address', ''),
                row.get('City/Town', ''),
                row.get('State', ''),
                row.get('ZIP Code', ''),
                row.get('Telephone Number', ''),
                row.get('Hospital Type', ''),
                row.get('emergency_services', 'Unknown')
            ))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    df_clean = load_and_clean_data('Hospital_General_Information.csv')
    insert_data_to_db(df_clean)