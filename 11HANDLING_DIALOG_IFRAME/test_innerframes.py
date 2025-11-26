import pytest
from playwright.sync_api import sync_playwright, expect,Page


def test_inner_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    # frame 3
    #frame3=page.frame_locator("frame[src='frame_3.html']") # grap teh frame 3
    frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html")  # grap teh frame 3

    frame3.locator("input[name='mytext3']").fill("Welcome") # get teh inputbox from frame 3 and provide teh text

    child_frames=frame3.child_frames
    print("Number of child frames inside teh frame 3: ", len(child_frames))

    innerframe=child_frames[0]

    radio=innerframe.get_by_label("I am a human")
    radio.check()
    expect(radio).to_be_checked()


    page.wait_for_timeout(5000)

