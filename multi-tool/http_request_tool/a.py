import requests

def send_request(url, verb):
    if url == 'https://dummytool.com/foobar':
        response = requests.Response()
        response.status_code = 200
        response.json = lambda: {"foo": "bar"}
        return {
            "response": response,
            "status_code": response.status_code,
            "success": True
        }
    else:
        response = requests.Response()
        response.status_code = 404
        return {
            "response": response,
            "status_code": response.status_code,
            "success": False
        }

# Mimic a GET request to 'https://dummytool.com/foobar'
result = send_request('https://dummytool.com/foobar', 'GET')
print(result)

# Mimic a GET request to 'https://dummydata/otherresource'
result = send_request('https://dummydata/otherresource', 'GET')
print(result)