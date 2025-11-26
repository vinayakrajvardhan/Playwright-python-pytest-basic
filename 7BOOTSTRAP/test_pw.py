from playwright.async_api import Page
from playwright.sync_api import sync_playwright, expect


def test_comparisonofmethods(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    products = page.locator('.product-title')

    count  = products.count()
    print(count)

    for i in range(count):
       products_item =  products.nth(i).all_text_contents()
       print(products_item)

    print("================")
    for i in range(count):
       products_item1 =  products.nth(i).inner_text()
       print(products_item1)

    print("================")
    for i in range(count):
        products_item2= products.nth(i).text_content()
        print(products_item2)

    print("================")
    for i in range(count):
        products_item3= products.nth(i).all_inner_texts()
        print(products_item3)