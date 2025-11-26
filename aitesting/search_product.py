import pytest
from playwright.sync_api import Page, expect


def test_search_tshirts(page: Page):
    """
    Test scenario: Search for T-shirts on automation practice website
    and verify that "Faded Short Sleeve T-shirts" is displayed in results
    """
    # Step 1: Navigate to the website
    page.goto('http://www.automationpractice.pl/index.php')

    # Step 2: Wait for page to load
    page.wait_for_load_state('networkidle')

    # Step 3: Find and fill the search box
    search_box = page.get_by_placeholder('Search')
    search_box.fill('T-shirts')

    # Step 4: Submit the search using locator
    search_button = page.locator('button[name="submit_search"]')
    search_button.click()

    # Step 5: Wait for results to load
    page.wait_for_load_state('networkidle')

    # Step 6: Verify that "Faded Short Sleeve T-shirts" is displayed in results
    # Target the product in the center column (search results area)
    product_name = page.locator('#center_column').get_by_text('Faded Short Sleeve T-shirts')
    expect(product_name).to_be_visible()

    print("✓ Test passed: 'Faded Short Sleeve T-shirts' found in search results")

