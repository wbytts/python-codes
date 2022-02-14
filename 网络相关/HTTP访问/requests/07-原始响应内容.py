import requests

r = requests.get('https://api.github.com/events', stream=True)
print(r.raw.read(10))
