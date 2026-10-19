import pytest

PRODUCT_IDS = [
    pytest.param(1, 200, id="product_1"),
    pytest.param(2, 200, id="product_2"),
    pytest.param(999, 404, id="not_found")
    ]

PRODUCT_SEARCH = [
    pytest.param({"q": "phone"}, 200, id="found"),
    pytest.param({"q": "kk"}, 200, id="empty_list")
]

PRODUCT_UPDATE = [
    pytest.param(25, {"title": "TEST"}, 200, id="update_title"),
    pytest.param(25, {"price": 99.9}, 200, id="update_price"),
    pytest.param(999, {"title": "TEST"}, 404, id="not_found")
]

PRODUCT_WITHOUT_TOKEN = [
    pytest.param(1, 401, id="valid_id_without_token"),
    pytest.param(999, 401, id="invalid_id_without_token")
]