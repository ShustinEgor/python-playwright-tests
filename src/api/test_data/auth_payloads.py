CREDS_PAYLOADS = [
    ({"username": "emilys", "password": "emilyspass"}, 200),
    ({"username": "invalidName", "password": "emilyspass"}, 400),
    ({"username": "emilys", "password": "invalidpass"}, 400),
    ({"username": "", "password": ""}, 400)
]