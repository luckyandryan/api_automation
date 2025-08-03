import requests
import logging

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": "reqres-free-v1"}

logger = logging.getLogger(__name__)


def create_user(name, job):
    payload = {
        "name": name,
        "job": job
    }

    response = requests.post(
        url=f"{BASE_URL}/users",
        json=payload,
        headers=HEADERS
    )

    logger.info(f"Status: {response.status_code} | Response: {response.json()}")

    return response


def get_user(user_id):
    response = requests.get(
        url=f"{BASE_URL}/users/{user_id}",
        headers=HEADERS
    )
    
    logger.info(f"Status: {response.status_code} | Response: {response.json()}")
    
    return response
