import sqlite3

def create_database():
    conn = sqlite3.connect('healthcare.db')  
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS hospitals')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hospitals (
            provider_id TEXT PRIMARY KEY,
            hospital_name TEXT NOT NULL,
            address TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            phone_number TEXT,
            hospital_type TEXT,
            emergency_services TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()