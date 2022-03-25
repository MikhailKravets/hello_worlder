import requests

if __name__ == '__main__':
    resp = requests.get("https://google.com")
    print(resp.status_code)
    print(resp.content)
