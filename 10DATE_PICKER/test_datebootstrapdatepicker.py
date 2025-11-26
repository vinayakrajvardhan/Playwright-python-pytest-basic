from playwright.sync_api import Page, expect


def select_checkin_date(page, year, month, day):
    while True:
        checkin_month_year = page.locator("h3[aria-live='polite']").nth(0).inner_text()
        current_month, current_year = checkin_month_year.split(" ")

        if current_month == month and current_year == year:
            break
        else:
            page.locator('button[aria-label="Next month"]').click()

    all_dates = page.locator('table.b8fcb0c66a tbody').nth(0).locator('td').all()
    for date in all_dates:
        if date.inner_text() == day:
            date.click()
            break



def select_checkout_date(page, year, month, day):
    while True:
        checkout_month_year = page.locator("h3[aria-live='polite']").nth(1).inner_text()
        current_month, current_year = checkout_month_year.split(" ")

        if current_month == month and current_year == year:
            break
        else:
            page.locator('button[aria-label="Next month"]').click()

    all_dates = page.locator('table.b8fcb0c66a tbody').nth(1).locator('td').all()
    for date in all_dates:
        if date.inner_text() == day:
            date.click()
            break

def test_bootstrap_datepicker(page: Page):
    page.goto("https://www.booking.com/")
    page.get_by_test_id("searchbox-dates-container").click()  # clicked on the date picker

    select_checkin_date(page, "2025", "October", "10")
    select_checkout_date(page, "2025", "November", "5")

    checkin_text = page.locator("span[data-testid='date-display-field-start']").inner_text()
    checkout_text = page.locator("span[data-testid='date-display-field-end']").inner_text()

    print("Check-in date:===>", checkin_text)
    print("Check-out date: ===>", checkout_text)

    expect(page.locator("span[data-testid='date-display-field-start']")).to_contain_text(checkin_text)
    expect(page.locator("span[data-testid='date-display-field-end']")).to_contain_text(checkout_text)

    page.wait_for_timeout(5000)