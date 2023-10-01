import requests

url = "http://localhost:5000"

def test_register_user():
    endpoint = "/api/register"
    data = {
        "username": "tes1t2213_user",
        "email": "test12213_user@example.com",
        "password": "test211_password",
        "full_name": "Tes1t22 User",
        "age": 30,
        "gender": "ghta"
    }
    response = requests.post(url + endpoint, json=data)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    assert response.status_code == 200
    assert response.json()["message"] == "User successfully registered!"

def test_generate_token():
    endpoint = "/api/token"
    data = {
        "username": "test_user",
        "password": "test_password"
    }
    response = requests.post(url + endpoint, json=data)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    assert response.status_code == 200
    assert response.json()["message"] == "Access token generated successfully."

def test_store_data():
    endpoint = "/api/data"
    data = {
        "key": "test_key",
        "value": "test_value"
    }
    response = requests.post(url + endpoint, json=data)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    assert response.status_code == 200
    assert response.json()["message"] == "Data stored successfully."

def test_retrieve_data():
    endpoint = "/api/data/test_key"
    response = requests.get(url + endpoint)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    assert response.status_code == 200
    assert response.json()["data"]["key"] == "test_key"
    assert response.json()["data"]["value"] == "test_value"

def test_update_data():
    endpoint = "/api/data/test_key"
    data = {
        "value": "new_test_value"
    }
    response = requests.put(url + endpoint, json=data)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    assert response.status_code == 200
    assert response.json()["message"] == "Data updated successfully."

def test_delete_data():
    endpoint = "/api/data/test_key"
    response = requests.delete(url + endpoint)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    assert response.status_code == 200
    assert response.json()["message"] == "Data deleted successfully."

def test_all():
    test_register_user()
    test_generate_token()
    test_store_data()
    test_retrieve_data()
    test_update_data()
    test_delete_data()

if __name__ == "__main__":
    test_all()