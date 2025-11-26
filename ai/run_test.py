

from playwright.sync_api import sync_playwright


def run_test():
    """Execute the API test"""
    print("\n" + "="*70)
    print("FAKE STORE API TEST - Using Playwright")
    print("="*70)

    with sync_playwright() as p:
        # Create a browser context and then a request context
        browser = p.chromium.launch()
        context = browser.new_context()
        api_context = context.request

        # Step 1: Set the API endpoint
        api_endpoint = 'https://fakestoreapi.com/products/1'
        print(f"\nStep 1: Setting API endpoint")
        print(f"  Endpoint: {api_endpoint}")

        # Step 2: Send GET request to the endpoint
        print(f"\nStep 2: Sending GET request to the endpoint")
        try:
            response = api_context.get(api_endpoint)
            print(f"  Request sent successfully")
        except Exception as e:
            print(f"  [FAILED] Failed to send request: {e}")
            return False

        # Step 3: Verify response status code is 200
        print(f"\nStep 3: Verifying response status code is 200")
        status = response.status
        print(f"  Received status: {status}")
        assert status == 200, f"Expected status 200, got {status}"
        print(f"  [PASSED] Status code verified: {status}")

        # Step 4: Get response body as JSON
        print(f"\nStep 4: Parsing response JSON")
        response_data = response.json()
        print(f"  [PASSED] Successfully parsed JSON response")

        # Step 5: Log the complete response body
        print(f"\nStep 5: Logging complete response body")
        print(f"  Complete Response Body:")
        import json
        print(json.dumps(response_data, indent=2))

        # Step 6: Validate required keys exist in response
        print(f"\nStep 6: Validating required keys in response")
        required_keys = ['id', 'title', 'price', 'category', 'description']
        for key in required_keys:
            if key not in response_data:
                print(f"  [FAILED] Required key '{key}' not found in response")
                return False
            print(f"  [PASSED] Key '{key}' found with value: {response_data[key]}")

        # Step 7: Verify expected values
        print(f"\nStep 7: Verifying expected values in response")
        expected_values = {
            'id': 1,
            'price': 109.95,
            'category': "men's clothing"
        }

        for key, expected_value in expected_values.items():
            actual_value = response_data.get(key)
            if actual_value != expected_value:
                print(f"  [FAILED] {key}: Expected {expected_value}, got {actual_value}")
                return False
            print(f"  [PASSED] {key}: {actual_value} (matches expected value)")

        print(f"\n" + "="*70)
        print("[SUCCESS] ALL TEST VALIDATIONS PASSED SUCCESSFULLY!")
        print("="*70 + "\n")

        # Close browser and context
        context.close()
        browser.close()
        return True


if __name__ == '__main__':
    try:
        success = run_test()

    except Exception as e:
        print(f"\n[ERROR] Test execution failed with error: {e}")
        import traceback
        traceback.print_exc()


