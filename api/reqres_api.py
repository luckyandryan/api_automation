from api.base import send_request

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": "reqres-free-v1"}


def create_user(name, job):
    payload = {"name": name, "job": job}

    response = send_request(
        method="POST", url=f"{BASE_URL}/users", payload=payload, headers=HEADERS
    )

    return response


def get_user(user_id):
    response = send_request(
        method="GET", url=f"{BASE_URL}/users/{user_id}", headers=HEADERS
    )

    return response
