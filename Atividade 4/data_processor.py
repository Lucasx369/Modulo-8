from datetime import datetime

def process_data(data):
    processed_data = {
        'data_ingestao': datetime.now(),
        'tipo': 'Text',
        'valor': data,
        'uso': 'previsao'
    }
    return processed_data
