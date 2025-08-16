import logging
import requests

logger = logging.getLogger(__name__)


def log_request_response(response, payload=None, headers=None):
    logger.info(
        f"Request: {response.request.method} {response.url} | Headers: {headers or '{}'} | Payload: {payload or '{}'}"
    )
    logger.info(f"Response: Status {response.status_code} {response.json()}")


def send_request(url, method="GET", headers=None, payload=None):
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=payload)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=payload)
        elif method.upper() == "PATCH":
            response = requests.patch(url, headers=headers, json=payload)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers)
        elif method.upper() == "HEAD":
            response = requests.head(url, headers=headers)
        else:
            logger.error(f"Unsupported HTTP method: {method}")
            return None

        log_request_response(response, payload, headers)
        return response
    except Exception as e:
        logger.error(f"Error sending request: {e}")
        return None
