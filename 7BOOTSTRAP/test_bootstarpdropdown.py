from playwright.sync_api import Page, expect

def test_input(page: Page):
    # Name
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.get_by_placeholder('Username').fill('Admin')
    page.get_by_placeholder('Password').fill('admin123')
    page.get_by_role('button',name='Login').click()

    page.get_by_text('PIM').click()

    # click on the Job title dropdown
    page.locator("form i").nth(2).click()  # this will open options from the dropdown
    page.wait_for_timeout(3000)

# capture all teh options from dropdown
    dropdown_option = page.locator('div[role="listbox"] span')
    print(dropdown_option.all_text_contents())
    print(dropdown_option.count())
    expect(dropdown_option).to_have_count(28)


    for i in range(dropdown_option.count()):
        print(dropdown_option.nth(i).text_content())
        print("=========================")
        print(dropdown_option.nth(i).inner_text())

    # select/click on specific option
    for i in range(dropdown_option.count()):
        text=dropdown_option.nth(i).inner_text()
        if text=='Finance Manager':
            print("Matching success.....")
            dropdown_option.nth(i).click()
            break

    page.wait_for_timeout(5000)