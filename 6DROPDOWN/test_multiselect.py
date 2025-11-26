from playwright.sync_api import Page, expect

def test_input(page: Page):
    # Name
    page.goto('https://testautomationpractice.blogspot.com/')
    page.get_by_label('Colors:').select_option(["Red","Blue","Green"])


    option_colors = page.locator('#colors>option')
    expect(option_colors).to_have_count(7)

    for option in option_colors.all_text_contents():
        print(option)
