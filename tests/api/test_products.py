import pytest

from src.api.http_client import api_get, api_put
from src.api.schemas.errors import ErrorBodyResponse
from src.api.schemas.product import ProductDetail, ProductSearch, ProductUpdate
from src.api.test_data.product_payloads import PRODUCT_IDS, PRODUCT_SEARCH, PRODUCT_UPDATE

@pytest.mark.parametrize("product_id, expected_status", PRODUCT_IDS)
def test_get_product(product_id, expected_status):
    response = api_get(f"/products/{product_id}")

    assert response.status_code == expected_status

    body = response.json()
    
    if expected_status == 404:
        error = ErrorBodyResponse(**body)
        assert error.message == f"Product with id '{product_id}' not found"
    elif expected_status == 200:
        product = ProductDetail(**body)
        assert product.id == product_id
    else:
        pytest.fail(f"для блока product статус {expected_status} пока не обрабатывается")

@pytest.mark.parametrize("params, expected_status", PRODUCT_SEARCH)
def test_get_search_product(params, expected_status):
    response = api_get("/products/search", params=params)
    assert response.status_code == expected_status
    body = response.json()

    search_result = ProductSearch(**body)

    if params["q"] == "phone":
        assert search_result.total > 0
        assert len(search_result.products) > 0

        ids = []
        for product in search_result.products:
            ids.append(product.id)

        assert 101 in ids, f"товара с id 101 нет в выдаче: {ids}"

    if params["q"] == "kk":
        assert search_result.total == 0
        assert search_result.products == []
        assert search_result.skip == 0
        assert search_result.limit == 0

@pytest.mark.parametrize("product_id, payload, expected_status", PRODUCT_UPDATE)
def test_product_update(product_id, payload, expected_status):
    response = api_put(f"/products/{product_id}", json=payload)
    assert response.status_code == expected_status
    body = response.json()

    if response.status_code == 200:
        product_update = ProductUpdate(**body)
        assert product_update.id == product_id
        for key, value in payload.items():
            assert body[key] == value
    elif response.status_code == 404:
        error = ErrorBodyResponse(**body)
        assert error.message == f"Product with id '{product_id}' not found"
    else:
        pytest.fail(f"такой {response.status_code} еще не обрабатывался")