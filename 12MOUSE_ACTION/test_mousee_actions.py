from playwright.sync_api import Page, expect



def test_mouse_action(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator('.dropbtn').hover()

    laptops = page.locator('.dropdown-content a').nth(1)

    laptops.hover()


def test_mouse_rightclick(page:Page):
    page.goto("http://swisnl.github.io/jQuery-contextMenu/demo.html")
    button = page.get_by_text('right click me',exact=True)
    button.click(button='right')

def test_mouse_doubleclick(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    button = page.locator("button[ondblclick='myFunction1()']")
    button.dblclick()

    text = page.locator('#field2')
    print(text.inner_text())
    expect(text).to_have_value('Hello World!')


def test_mouse_draganddrop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    source = page.locator("div[id='draggable'] p")
    target = page.locator("#droppable")

    # Appraoch1 : manual drag using hover()
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    # Appraoch 2 : drag_to()
    source.drag_to(target)

    page.wait_for_timeout(5000)

