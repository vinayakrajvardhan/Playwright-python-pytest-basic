from playwright.sync_api import expect,Page


def test_static_table(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    # locating table
    table = page.locator('table[name="BookTable"] tbody')
    print(table.inner_text())
    expect(table).to_be_visible()

    # 1. count total number of rows in a table
    rows = table.locator('tr')
    print(rows.count())
    expect(rows).to_have_count(7)

    # 2. count total number of columns/headers in table
    column = rows.locator('th')
    expect(column).to_have_count(4)

    # 3. Read all the data from 2nd row of the table
    second_rows = rows.nth(2).locator('td')
    print(second_rows.all_inner_texts())

    #4. Read all the data from teh table ( Excluding header)
    all_row_data=rows.all()

    # print("Printing data from all teh rows and collumns.......")
    for row in all_row_data[1:]:
        for col in row.locator('td').all_inner_texts():
            print(col)

    # 5. Print Book names whose author is 'Mukesh'
    print("Printing Books names written By Mukesh........")
    for row in all_row_data[1:]:
        author_name = row.locator('td').nth(1).inner_text()
        if author_name == 'Mukesh':
            book_name = row.locator('td').nth(0).inner_text()
            print(f"{author_name} \t {book_name}")


    #6. Calculate total price of all teh books
    total_price=0
    for row in all_row_data[1:]:
        price = row.locator('td').nth(3).inner_text()
        total_price = total_price  + int(price)
    print("Total price:", total_price)



