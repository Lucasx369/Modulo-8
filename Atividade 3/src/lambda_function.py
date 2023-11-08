import base64
import json

users = {
    "afonso": "inteli123",
    "lucas": "inteliabc",
}

def lambda_handler(event, context):
    headers = event.get('headers', {})
    authorization_header = headers.get('Authorization', '')

    if not authorization_header:
        return {
            'statusCode': 401,
            'body': 'Acesso não autorizado'
        }

    if authorization_header.startswith('Basic '):
        encoded_credentials = authorization_header[len('Basic '):]
        credentials = base64.b64decode(encoded_credentials).decode('utf-8')

        user, password = credentials.split(':')

        if user in users and users[user] == password:
            return {
                'statusCode': 200,
                'body': json.dumps(event['body'])
            }

    return {
        'statusCode': 401,
        'body': 'Acesso não autorizado'
    }