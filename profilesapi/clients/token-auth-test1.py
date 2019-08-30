import requests


def client():
    print('test')
    # credentials = {"username": "admin", "password": "fake"}

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)
    token_h = "Token 1627aef5ee2dec282eb59c577bd90ede498e275e"
    headers = {"Authorization": token_h}
    response = requests.get(
        "http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
