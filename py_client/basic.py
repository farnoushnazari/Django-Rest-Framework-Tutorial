import requests

# endpoint = "http://localhost:8000/"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(
    endpoint, 
    json={'title': 'hello world again', 'content': 'abc', 'price': 30}
)
print(get_response.json())