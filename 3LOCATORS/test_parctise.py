from playwright.sync_api import Page, expect



def test_orange_site(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login")
    print(page.url)
    print(page.title())
    expect(page.get_by_role("heading",name="Dashboard"))
    expect(page.get_by_role("img",name="client brand banner"))

