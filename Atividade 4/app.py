from flask import Flask, jsonify

from weather_api import get_weather_data
from data_processor import process_data
from data_storage import store_data

import sqlite3
import json

app = Flask(__name__)

def get_all_data():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM weather_data")
    data = cursor.fetchall()

    conn.close()
    
    columns = ['data_ingestao', 'tipo', 'valor', 'uso']
    result = [dict(zip(columns, row)) for row in data]
    
    return result


@app.route('/')
def index():
    return "ETL Application"

@app.route('/run-etl')
def run_etl():
    cities = ["São Paulo", "Rio de Janeiro", "Curitiba", "Campo Grande", "Salvador", "Recife", "Manaus", "Goiânia", "Niterói", "Bonito"]  # Lista de cidades
    api_key = "d1a60b029f36bb0ca25230acee600c60"

    for city in cities:
        raw_data = get_weather_data(api_key, city)
        if raw_data:
            processed_data = process_data(raw_data)
            store_data(processed_data)

    all_data = get_all_data()
    return jsonify(all_data)

if __name__ == '__main__':
    app.run(debug=True)