import pytest
from playwright.sync_api import Page, expect

def test_input(page: Page):
    # Name
    page.goto('https://testautomationpractice.blogspot.com/')
    input_name = page.get_by_placeholder('Enter Name')
    input_name.fill('raj')
    expect(input_name).to_be_visible()
    expect(input_name).to_be_enabled()
    expect(input_name).to_have_attribute('maxlength','15')
    max_lenght = input_name.get_attribute('maxlength')
    print(max_lenght)

    # Radio button
    male_radio = page.locator("#male")

    # visibility of teh element and enable or not
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    # Male radio button should not be checked ( default)
    expect(male_radio).not_to_be_checked()

    # Select/Check radio button - action
    male_radio.check()

    # Male radio button should not be checked ( default)
    expect(male_radio).to_be_checked()





