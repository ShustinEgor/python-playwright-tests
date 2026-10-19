import pytest

from src.api.http_client import api_get, api_post, api_delete
from src.api.schemas.cart import Cart, CartDetail, DeletedCart
from src.api.schemas.errors import ErrorBodyResponse
from src.api.test_data.cart_payloads import CART_PAYLOADS, CART_IDS, DELETE_CART_IDS
import re

@pytest.mark.parametrize("payload", CART_PAYLOADS)
def test_add_cart(payload):
	response = api_post("/carts/add", json=payload)

	assert response.status_code == 201
	body = response.json()

	cart = Cart(**body)
	assert cart.userId == payload["userId"]
	assert cart.totalProducts == len(payload["products"])

@pytest.mark.parametrize("cart_id, expected_status", CART_IDS)
def test_get_cart(cart_id, expected_status):
    response = api_get(f"/carts/{cart_id}")

    assert response.status_code == expected_status
    body = response.json()

    if expected_status == 404:
        error = ErrorBodyResponse(**body)
        assert error.message  == f"Cart with id '{cart_id}' not found"
    elif expected_status == 200:
        cart = CartDetail(**body)
        assert cart.id == cart_id
    else:
         pytest.fail(f"для блока cart статус {expected_status} пока не обрабатывается")  
         

@pytest.mark.parametrize("cart_id", DELETE_CART_IDS)
def test_delete_carts(cart_id):
     response = api_delete(f"/carts/{cart_id}")

     assert response.status_code == 200
     body = response.json()

     cart = DeletedCart(**body)
     assert cart.id == cart_id
     assert cart.isDeleted == True
     assert re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$", cart.deletedOn)

     
