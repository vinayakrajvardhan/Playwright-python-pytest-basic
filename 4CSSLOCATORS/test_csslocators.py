'''
tag id          tag#id
tag class       tag.class
tag attribute   tag[attribute=value]
tag class attribute     tag.class[attribute=value]

'''



import pytest
from playwright.sync_api import Page, expect

def test_verify_css_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    #tag id
    # page.wait_for_selector('#small-searchterms').fill('T shirt')
    # page.get_by_role('button',name='Search').click()

    #tag class
    # page.locator('input.search-box-text.ui-autocomplete-input').fill('T shirt')
    # page.get_by_role('button', name='Search').click()

    # tag attribute
    # page.locator('input[name=q]').fill('T shirt')
    # page.get_by_role('button', name='Search').click()

    # tag class attribute
    # page.locator("input.search-box-text[value='Search store']").fill("T-Shirts")
    # page.get_by_role('button', name='Search').click()

    page.locator()

