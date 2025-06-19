import requests

def test_amazon_home_status():
    response = requests.get("https://www.amazon.com")
    assert response.status_code == 200
    
