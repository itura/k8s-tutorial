import os
import sys
import requests

if len(sys.argv) == 2:
    service_url = f'http://{sys.argv[1]}'
else:
    host = os.environ.get('HELLO_WORLD_SERVICE_SERVICE_HOST')
    port = os.environ.get('HELLO_WORLD_SERVICE_SERVICE_PORT')
    service_url = f'http://{host}:{port}'

print(f'Using {service_url}')

response = requests.get(service_url)

print(f'Received {response.status_code}: {response.text}')

