import pytest
from playwright.sync_api import expect,Page

def test_shadow_dow(page:Page):
    page.goto('https://books-pwakit.appspot.com/')
    search_box = page.get_by_role("searchbox", name="Search Books")
    search_box.fill("hello")
    page.get_by_role("button",name="search by voice").click()


