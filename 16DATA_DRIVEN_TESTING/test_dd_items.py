import pytest

from playwright.sync_api import expect,Playwright,Page


# Test data
search_items = ['laptop', 'Gift card', 'smartphone', 'monitor']

@pytest.mark.parametrize("items",search_items)
def test_search_item(items,page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    page.locator('#small-searchterms').fill(items)
    page.locator('input.button-1.search-box-button').click()

    # Assertion: first result title should contain the search item
    first_result = page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(items, ignore_case=True)

