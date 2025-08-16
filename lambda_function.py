import requests

def lambda_handler(event, context):
    response = requests.get('https://api.github.com/zen')
    return {
        'statusCode': 200,
        'body': f'Hello Github actions for lambda! GitHub says: {response.text}'
    }

if __name__ == "__main__":    
    print(lambda_handler({}, {}))