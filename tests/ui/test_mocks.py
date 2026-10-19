from playwright.sync_api import Page, Route, expect
import pytest
from src.config import BASE_URL_UI, USERNAME_UI, PASSWORD_UI

MOCK_URL = "https://demo.playwright.dev/api-mocking"

def test_mock_fruits(page: Page):

    def handle(route: Route):
        route.fulfill(json=[{"name": "Strawberry", "id": 21}])

    page.route("*/**/api/v1/fruits", handle)

    page.goto(MOCK_URL)

    expect(page.get_by_text("Strawberry")).to_be_visible()


def test_mocks_saucedemo(page: Page):
    
    def handle(route: Route):
        print("blocked:", route.request.url)
        route.abort()
    
    page.route("*/**/*.jpg", handle)

    page.goto(BASE_URL_UI)
    page.get_by_role("textbox", name="Username").fill(USERNAME_UI)
    page.get_by_role("textbox", name="Password").fill(PASSWORD_UI)
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_role("button", name="Add to cart")).to_have_count(6)
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

def test_mock_fruits_empty(page: Page):

    def handle(route: Route):
        route.fulfill(json=[])

    page.route("*/**/api/v1/fruits", handle)

    page.goto(MOCK_URL)

    expect(page.get_by_role("list")).to_be_attached()
    expect(page.get_by_role("listitem")).to_have_count(0)

def test_mock_fruits_error(page: Page):

    def handle(route: Route):
        route.fulfill(status=500)

    page.route("*/**/api/v1/fruits", handle)

    page.goto(MOCK_URL)

    expect(page.get_by_text("Loading")).to_be_visible()