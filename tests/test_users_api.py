from datetime import datetime
from api import reqres_api
from utils.assertions import AssertionHelper

assertion = AssertionHelper()


def test_create_user():
    response = reqres_api.create_user(name="Lucky", job="QA")
    data = response.json()

    assertion.assert_equal(response.status_code, 201)
    assertion.assert_key_exists("id", data)
    assertion.assert_key_exists("createdAt", data)
    assertion.assert_key_exists("name", data)
    assertion.assert_key_exists("job", data)
    assertion.assert_equal(data["name"], "Lucky")
    assertion.assert_equal(data["job"], "QA")
    
    created_at_date = datetime.strptime(data["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ").date()
    today_date = datetime.now().date()
    assertion.assert_equal(created_at_date, today_date)


def test_get_existing_user():
    response = reqres_api.get_user(user_id=2)
    data = response.json()

    user = data["data"]
    assertion.assert_equal(response.status_code, 200)
    assertion.assert_equal(user["id"], 2)
    assertion.assert_data_type(user["id"], int)
    assertion.assert_key_exists("id", user)
    assertion.assert_key_exists("email", user)
    assertion.assert_key_exists("first_name", user)
    assertion.assert_key_exists("last_name", user)
    assertion.assert_key_exists("avatar", user)
    assertion.assert_in("@", user["email"])
    assertion.assert_valid_email(user["email"])
    assertion.assert_in(".jpg", user["avatar"])
    assertion.assert_startswith(user["avatar"], "https://reqres.in/img/")

    support = data["support"]
    assertion.assert_key_exists("url", support)
    assertion.assert_key_exists("text", support)
    assertion.assert_startswith(support["url"], "https://")
    assertion.assert_in("contentcaddy.io", support["url"])
    assertion.assert_in("social media", support["text"].lower())


def test_get_non_existing_user():
    response = reqres_api.get_user(user_id=23)
    data = response.json()

    assertion.assert_equal(response.status_code, 404)
    assertion.assert_equal(data, {})
