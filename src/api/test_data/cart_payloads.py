import pytest

CART_PAYLOADS = [
    pytest.param({"userId": 1, "products": [{"id": 144, "quantity": 1}]}, id='one_product'),
    pytest.param({"userId": 2, "products": [{"id": 144, "quantity": 4}, {"id":98, "quantity": 1}]}, id="two_products"),
    pytest.param({"userId": 3, "products": [{"id": 1, "quantity": 10}]}, id="big_quantity"),
]

CART_IDS = [
    pytest.param(1, 200, id="cart1"),
    pytest.param(2, 200, id="cart2"),
    pytest.param(999, 404, id="not_found")
    ]

DELETE_CART_IDS = [1]



