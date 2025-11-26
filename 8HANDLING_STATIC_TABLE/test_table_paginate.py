from playwright.sync_api import expect,Page


def test_static_table(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    # locating table
    tables = page.locator('div.table-container')
    table_values = tables.all_inner_texts()
    for val in table_values:
        print(val)


    # rows
    rows = tables.locator('tr')
    rows_values = rows.all_inner_texts()
    for val in rows_values:
        print(val)

    # columns
    columns = tables.locator('tbody td')
    columns_values = columns.all_inner_texts()
    for val in columns_values:
        print(val)


    print('============================')
    page.locator('ul.pagination li a').nth(2).click()
    # locating table
    tables = page.locator('div.table-container')
    table_values = tables.all_inner_texts()
    for val in table_values:
        print(val)
