import os

value = os.environ.get('HELLO_WHAT') or 'World'

print('Hello ' + value)
