from src.schemas.cart import Cart

def test_add_cart(api_context):
	payload = {
		"userId": 1,
		"products": [
			{"id": 144, "quantity": 4},
			{"id": 98, "quantity": 1},
		],
	}

	response = api_context.post("/carts/add", data = payload)

	assert response.ok
	body = response.json()

	cart = Cart(**body)
	assert cart.userId == payload["userId"]
	assert cart.totalProducts == len(payload["products"])



