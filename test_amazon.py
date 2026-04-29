import pytest
from playwright.sync_api import sync_playwright

def search_and_add_to_cart(page, product_name):
    page.goto("https://www.amazon.com")

    # Handle popup (multiple ways)
    try:
        page.locator("text=Dismiss").click(timeout=3000)
    except:
        pass

    page.keyboard.press("Escape")

    # Search product
    page.fill("#twotabsearchtextbox", product_name)
    page.press("#twotabsearchtextbox", "Enter")

    # Wait for results properly
    page.wait_for_selector(".s-main-slot", timeout=10000)

    # Wait extra for safety
    page.wait_for_timeout(3000)

    # Ensure products are loaded
    page.locator(".s-main-slot h2 a").first.wait_for(timeout=10000)

    # Click first product (handle new tab)
    with page.context.expect_page() as new_page_info:
        page.locator(".s-main-slot h2 a").first.click()

    product_page = new_page_info.value
    product_page.wait_for_load_state()

    # Get price (robust selector)
    price = product_page.locator("span.a-price span.a-offscreen").first.text_content()
    print(f"{product_name} Price: {price}")

    # Add to cart
    product_page.locator("#add-to-cart-button").click()

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


def test_search_iphone(browser):
    context = browser.new_context()
    page = context.new_page()
    search_and_add_to_cart(page, "iPhone")
    context.close()


def test_search_galaxy(browser):
    context = browser.new_context()
    page = context.new_page()
    search_and_add_to_cart(page, "Samsung Galaxy")
    context.close()