from playwright.sync_api import Page,expect
import re

# 1) page.get_by_alt_text()
# 2) page.get_by_text()
# 3) page.get_by_role()
# 4) page.get_by_label()
# 5) page.get_by_placeholder()
# 6) page.get_by_title()
# 7) page.get_by_test_id()

def test_verify_pwlocators(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    #time.sleep(5) # seconds
    # page.wait_for_timeout(5000) # 500 ms = 5 secs

    # 1) page.get_by_alt_text()
    logo = page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()

    #  2) page.get_by_text()
    page.get_by_text("Welcome to our store")
    expect(page.get_by_text("Welcome to")).to_be_visible()
    expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()

    # 3) page.get_by_role()
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    button_register = page.get_by_role("button",name="register")
    expect(button_register).to_be_visible()
    button_register.click()

    # 4) page.get_by_label()
    page.get_by_label("First name").fill("John")
    page.get_by_label("Last name").fill("doe")
    page.get_by_label("Email").fill("john@gmail.com")

    # 5) page.get_by_placeholder()
    page.get_by_placeholder("Search store").fill("Apple MacBook Pro")


    # 6) page.get_by_title()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_title("HyperText Markup Language")
    expect(page.get_by_title("HyperText Markup Language")).to_be_visible()

    # 7) page.get_by_test_id()
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
















