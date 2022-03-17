import requests

r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r.text)
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
print(r.text)
r = requests.delete('http://httpbin.org/delete')
print(r.text)
r = requests.head('http://httpbin.org/get')
print(r.text)
r = requests.options('http://httpbin.org/get')
print(r.text)





