import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_dialog(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    # Approach 1
    # registering an event
    def handle_dialog(dialog):
        dialog.accept()
    page.on("dialog",handle_dialog)
    page.locator('#alertBtn').click()
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_dialog2(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    # Approach 1
    # registering an event

    page.on("dialog",lambda dialog:dialog.accept())
    page.locator('#alertBtn').click()
    page.wait_for_timeout(5000)

def test_dialog3(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    page.on('dialog',lambda dialog:dialog.dismiss())

    page.locator('#confirmBtn').click()

    text = page.locator('#demo').inner_text()
    print(text)
    expect(text).to_have_text('You pressed Cancel!')



def test_dialog4(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    page.on('dialog',lambda dialog:dialog.accept('John'))

    page.locator('#promptBtn').click()

    text = page.locator('#demo').inner_text()
    print(text)
   




