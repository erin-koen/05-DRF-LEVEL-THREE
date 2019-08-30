import requests


def client():
    # data = {"username": "FakeUser1",
    #         "email": "test@rest.com",
    #         "password1": "fake1234",
    #         "password2": "fake1234"
    #         }

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/',
    #                          data=data)
    token_h = "Token e80a32f16261b416902aa74f49bd86391d98b84f"
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()