from playwright.sync_api import sync_playwright, expect


def test_search_tshirts_sync():
    """
    Test scenario: Search for T-shirts on automation practice website
    and verify that "Faded Short Sleeve T-shirts" is displayed in results
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to False for visible browser
        page = browser.new_page()

        try:
            # Step 1: Navigate to the website
            print("Step 1: Navigating to http://www.automationpractice.pl/index.php")
            page.goto('http://www.automationpractice.pl/index.php')

            # Step 2: Wait for page to load
            print("Step 2: Waiting for page to load")
            page.wait_for_load_state('networkidle')

            # Step 3: Find and fill the search box
            print("Step 3: Finding and filling search box with 'T-shirts'")
            search_box = page.get_by_placeholder('Search')
            search_box.fill('T-shirts')

            # Step 4: Submit the search using locator
            print("Step 4: Submitting search")
            search_button = page.locator('button[name="submit_search"]')
            search_button.click()

            # Step 5: Wait for results to load
            print("Step 5: Waiting for results to load")
            page.wait_for_load_state('networkidle')

            # Step 6: Verify that "Faded Short Sleeve T-shirts" is displayed in results
            print("Step 6: Verifying product is displayed in results")
            # Target the product in the center column (search results area)
            product_name = page.locator('#center_column').get_by_text('Faded Short Sleeve T-shirts')
            expect(product_name).to_be_visible()

            print("✓ Test passed: 'Faded Short Sleeve T-shirts' found in search results")
            return True

        except Exception as e:
            print(f"✗ Test failed: {str(e)}")
            return False
        finally:
            browser.close()


if __name__ == '__main__':
    success = test_search_tshirts_sync()
    exit(0 if success else 1)

