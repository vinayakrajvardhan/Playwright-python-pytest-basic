from playwright.sync_api import Page, expect

def test_input(page: Page):
    # Name
    page.goto('https://testautomationpractice.blogspot.com/')

    # country_dropdown = page.get_by_label('Country:')
    country_dropdown = page.get_by_role('combobox',name='Country:')
    print(country_dropdown.input_value())
    country_dropdown.select_option('United Kingdom')

#   all options
    input_value  = page.locator('#country>option')
    expect(input_value).to_have_count(10)

    option_text = [text.strip() for text in input_value.all_text_contents()]
    print(option_text)

    for option in option_text:
        print(option)
