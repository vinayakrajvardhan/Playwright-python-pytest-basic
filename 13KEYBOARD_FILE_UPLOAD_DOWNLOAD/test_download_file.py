from playwright.sync_api import expect, Page
import os


def test_download_file(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.get_by_role("textbox",name="Enter Text:").fill("Welcome")
    page.get_by_role("button",name="Generate and Download Text File").click()

    # Approach1
    # def handle_download(download):
    #     download.save_as("downloads/testfile.txt")
    # page.on("download",handle_download)

    # Approach1
    page.on("download", lambda download:download.save_as("downloads/testfile.txt"))

    page.locator("#txtDownloadLink").click()

    if os.path.exists("downloads/testfile.txt"):
        print("File exists")
    else:
        print("File not exist")

