import requests

def mock_request(url, verb):
    if url == 'https://dummytool.com/foobar':
        data = {"foo": "bar"}
        status_code = 200
        success = True
    else:
        data = {"error": "Not Found"}
        status_code = 404
        success = False

    response = {
        "data": data,
        "status_code": status_code,
        "success": success
    }

    return response

# Mimic a GET request to 'https://dummytool.com/foobar'
print(mock_request('https://dummytool.com/foobar', 'GET'))

# Mimic a GET request to 'https://dummydata/otherresource'
print(mock_request('https://dummydata/otherresource', 'GET'))