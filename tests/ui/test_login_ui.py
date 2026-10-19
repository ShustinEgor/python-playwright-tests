import re
import pytest
from playwright.sync_api import Page, expect
from src.config import BASE_URL_UI, USERNAME_UI, PASSWORD_UI
from src.ui.test_data.auth_payloads import CREDS_PAYLOADS

def test_login_success(page: Page):
    page.goto(BASE_URL_UI)
    page.get_by_role("textbox", name="Username").fill(USERNAME_UI)
    page.get_by_role("textbox", name="Password").fill(PASSWORD_UI)
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(re.compile("inventory"))
    expect(page.get_by_text("Products", exact=True)).to_be_visible()

@pytest.mark.parametrize("payload, alert", CREDS_PAYLOADS, ids=["locked_out_user", "empty_fields", "empty_pass", "invalid_pass"])
def test_login_negative(page: Page, payload, alert):
    page.goto(BASE_URL_UI)
    page.get_by_role("textbox", name="Username").fill(payload["username"])
    page.get_by_role("textbox", name="Password").fill(payload["password"])
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("alert")).to_contain_text(alert)