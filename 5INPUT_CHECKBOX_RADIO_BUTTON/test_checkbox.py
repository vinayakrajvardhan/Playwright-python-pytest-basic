from playwright.sync_api import Page, expect

def test_input(page: Page):
    # Name
    page.goto('https://testautomationpractice.blogspot.com/')
    input_name = page.get_by_placeholder('Enter Name')

    # checkbox
    # input_checkbox = page.get_by_role('checkbox', name='Sunday')
    # expect(input_checkbox).to_be_editable()
    # input_checkbox.click()
    # expect(input_checkbox).to_be_enabled()

    # 2. count number of check boxes
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes = []
    for day in days:
        checkbox = page.get_by_label(day)
        checkboxes.append(checkbox)

    checkboxes = [page.get_by_label(day) for day in days]
    print("total number of checkboxes:", len(checkboxes))

    # 3 . select all the checkboxes and assert each check box is selected
    # for checkbox in checkboxes:
    #     checkbox.check()
    #     expect(checkbox).to_be_checked()

    # 4. check last 3 checkboxes
    for checkbox in checkboxes[3:]:
        checkbox.check()
        expect(checkbox).to_be_checked()

    # 5. Toggle checkboxes.
    for checkbox in checkboxes:
        if checkbox.is_checked():
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
        else:
            checkbox.check()
            expect(checkbox).to_be_checked()

    # 6. Randomly check checkboxes - check 1,3 6 checkboxes
    # indexes=[1,3,6]
    #
    # for i in indexes:
    #     checkboxes[i].check()
    #     expect(checkboxes[i]).to_be_checked()
    #
    # page.wait_for_timeout(5000)

    # 7. select checkbox based on the label/input value by choice
    weekday = "Friday"

    for label in days:
        if label == weekday:
            checkbox = page.get_by_label(label)
            checkbox.check()
            expect(checkbox).to_be_checked()



