from playwright.sync_api import expect,Page

def test_verifyPage(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")
    print(page.title())
    print(page.url)
    expect(page).to_have_url("http://www.automationpractice.pl/index.php")
    expect(page).to_have_title("My Shop")
