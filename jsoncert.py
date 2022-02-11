import json

import requests
# from requests import Request, Session
CERT = '6316dc322e44e871713ce38804a07789ae20f0c9'
KEY = 'EDF27F8CC7553D8C7ED5883F81AB4318C817618A16D9EEF1145E198FFCFD26C0'


def main():
    url = "https://slb.medv.ru/api/v2/"
    headers = {
        'content-type': 'application/json',
        'Authorization': CERT,
    }
    payload = {
        "method": "auth.check",
        "params": [],
        "jsonrpc": "2.0",
        "id": 1,
    }
    # cert = (CERT, KEY)
    # s = requests.Session()
    # s.cert = cert
    # s.headers = {
    #     'content-type': 'application/json',
    # }
    # s.params = {
    #     "method": "auth.check",
    #     "params": [],
    #     "jsonrpc": "2.0",
    #     "id": 1,
    # }
    cert = (CERT, KEY)
    response = requests.get(url, data=json.dumps(payload), headers=headers, cert=cert).json()
    # response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    print(response)


# with requests.Session() as session:
#     url = "https://slb.medv.ru/api/v2/"
#     headers = {
#         'content-type': 'application/json',
#         'Authorization': CERT,
#     }
#
#     # Example echo method
#     payload = {
#         "method": "auth.check",
#         "params": [],
#         "jsonrpc": "2.0",
#         "id": 1,
#     }
#     cert = (CERT, KEY)
#     response = requests.get(url, data=json.dumps(payload), headers=headers, cert=cert).json()
#     print(response)
if __name__ == "__main__":
    main()
