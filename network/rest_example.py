import requests

if __name__ == '__main__':
    resp = requests.get("http://ron-swanson-quotes.herokuapp.com/v2/quotes")
    print(resp.status_code)
    print(resp.json())
