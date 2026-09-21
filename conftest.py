import pytest

BASE_URL = "https://dummyjson.com"


@pytest.fixture(scope="session")
def api_context(playwright):
    context = playwright.request.new_context(base_url=BASE_URL)
    yield context
    context.dispose()


