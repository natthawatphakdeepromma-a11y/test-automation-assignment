import requests

BASE_URL = "https://reqres.in/api/users"
HEADERS = {"x-api-key": "pub_6374ee644aa39f16c524cc7edd9d3b27d52a45a5dd9d611ef478179fcb586891"}
 
def test_get_user_profile_success():
    response = requests.get(f"{BASE_URL}/12", headers=HEADERS)

    assert response.status_code == 200

    data = response.json().get("data", {})
    assert data.get("id") == 12
    assert data.get("email") == "rachel.howell@reqres.in"
    assert data.get("first_name") == "Rachel"
    assert data.get("last_name") == "Howell"
    assert data.get("avatar") == "https://reqres.in/img/faces/12-image.jpg"


def test_get_user_profile_not_found():
    response = requests.get(f"{BASE_URL}/1234", headers=HEADERS)
    assert response.status_code == 404
    assert response.json() == {}