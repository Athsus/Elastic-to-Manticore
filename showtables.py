import requests

response = requests.post('http://localhost:9308/sql', data={'mode': 'raw', 'query': 'SHOW TABLES'})
print(response.text)
