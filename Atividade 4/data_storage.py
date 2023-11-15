import sqlite3

def store_data(data):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather_data (data_ingestao TEXT, tipo TEXT, valor TEXT, uso TEXT)''')
    c.execute("INSERT INTO weather_data VALUES (?, ?, ?, ?)", (data['data_ingestao'], data['tipo'], str(data['valor']), data['uso']))
    conn.commit()
    conn.close()
