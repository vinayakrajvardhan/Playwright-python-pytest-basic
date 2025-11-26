import pytest
from playwright.sync_api import sync_playwright, expect,Page


def test_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames=page.frames
    print("Number of frames on a page:", len(frames))  # 7

    # frame 1
    #frame1=page.frame("name of the frame")  # options 3: get the frame using name  ( We cannot use here since we do not have name for the frame 1
    #frame1=page.frame_locator("frame[src='frame_1.html']")  # option 1: get the frame using css
    frame1= page.frame(url='https://ui.vision/demo/webtest/frames/frame_1.html') # option 2: get the frame using url
    inputbox=frame1.locator("input[name='mytext1']")
    inputbox.fill("Welcome")

    expect(inputbox).to_have_value("Welcome")

    page.wait_for_timeout(5000)

