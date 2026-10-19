from src.config import PASSWORD_UI

CREDS_PAYLOADS = [
    ({"username": "locked_out_user", "password": PASSWORD_UI}, "locked out"),
    ({"username": "", "password": ""}, "Username is required"),
    ({"username": "standard_user", "password": ""}, "Password is required"),
    ({"username": "standard_user", "password": "invalidPass"}, "do not match")
]