import requests

# print(requests.get("http://127.0.0.1:8000/").json())

# print(requests.get("http://127.0.0.1:8000/items/1234").json())

print(requests.get("http://127.0.0.1:8000/genero/2014").json())
print(requests.get("http://127.0.0.1:8000/genero/2015").json())
print(requests.get("http://127.0.0.1:8000/genero/2016").json())
print(requests.get("http://127.0.0.1:8000/genero/2017").json())
print(requests.get("http://127.0.0.1:8000/genero/2018").json())


# print(requests.get("http://127.0.0.1:8000/test/1888").json())