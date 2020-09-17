import json
from urllib import request
# import requests
from urllib.parse import urlencode
from urllib.request import urlopen, Request, URLopener

cert = 'client03test.crt'
key = 'client03test.key'
url = "https://slb.medv.ru/api/v2/"
headers = {
    'content-type': 'application/json',
}
values = {
    "method": "auth.check",
    "params": [],
    "jsonrpc": "2.0",
    "id": 1,
}


# def main():
#     url = "https://slb.medv.ru/api/v2/"
#     headers = {
#         'content-type': 'application/json',
#     }
#     payload = {
#         "method": "auth.check",
#         "params": [],
#         "jsonrpc": "2.0",
#         "id": 1,
#     }
#
#     # response = requests.post(url, cert=(cert, key), verify=True, headers=headers, data=json.dumps(payload))
#     response = requests.post(url, cert=(CERTIFICATE, KEY), verify=True, headers=headers, data=json.dumps(payload))
#     print(response.json())


def main2():
    # res = request.Request(url=url, headers=headers, )
    data = urlencode(values).encode()
    URLopener(key_file=key, cert_file=cert)
    print(urlopen(Request(url=url, data=data, headers=headers, ), timeout=60).read().decode())

    # response = requests.post(url, cert=(cert, key), verify=True, headers=headers, data=json.dumps(payload))
    # response = requests.post(url, cert=(CERTIFICATE, KEY), verify=True, headers=headers, data=json.dumps(payload))
    # print(response.json())


if __name__ == "__main__":
    # main()
    main2()
