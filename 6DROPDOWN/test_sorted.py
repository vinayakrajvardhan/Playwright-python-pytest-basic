import copy

from playwright.sync_api import Page, expect

def test_input(page: Page):
    # Name
    page.goto('https://testautomationpractice.blogspot.com/')
    page.get_by_label('Sorted List:').select_option(["Cat","Deer"])

    colors_options = page.locator("#animals>option")
    print(colors_options.count())
    expect(colors_options).to_have_count(10)
    # for option in colors_options.all_text_contents():
    #     print(option,end=" ")

    animal_list =  colors_options.all_text_contents()

    animal_list2 = animal_list.copy()
    print(animal_list)
    print(sorted(animal_list2))


