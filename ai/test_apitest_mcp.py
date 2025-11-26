"""
Playwright + pytest API Test Script
Tests the Fake Store API for product details validation
"""
import pytest
from playwright.sync_api import sync_playwright


def test_fake_store_api_validation():
    """
    Test scenario: Validate product details from Fake Store API
    - Set API endpoint to https://fakestoreapi.com/products/1
    - Send GET request to the endpoint
    - Verify response status code is 200
    - Validate response JSON contains required keys
    - Verify expected values in response
    - Log complete response body
    """
    with sync_playwright() as p:
        # Create a browser context for making API calls
        browser = p.chromium.launch()
        context = browser.new_context()
        api_context = context.request

        # Step 1: Set the API endpoint
        api_endpoint = 'https://fakestoreapi.com/products/1'
        print(f"\n{'='*70}")
        print(f"Step 1: Setting API endpoint to {api_endpoint}")
        print(f"{'='*70}")

        # Step 2: Send GET request to the endpoint
        print(f"\nStep 2: Sending GET request to the endpoint")
        response = api_context.get(api_endpoint)

        # Step 3: Verify response status code is 200
        print(f"\nStep 3: Verifying response status code is 200")
        assert response.status == 200, f"Expected status 200, got {response.status}"
        print(f"[PASSED] Status code verified: {response.status}")

        # Step 4: Get response body as JSON
        print(f"\nStep 4: Parsing response JSON")
        response_data = response.json()

        # Step 5: Log the complete response body
        print(f"\nStep 5: Logging complete response body")
        print(f"Complete Response Body:")
        print(f"{response_data}")

        # Step 6: Validate required keys exist in response
        print(f"\nStep 6: Validating required keys in response")
        required_keys = ['id', 'title', 'price', 'category', 'description']
        for key in required_keys:
            assert key in response_data, f"Required key '{key}' not found in response"
            print(f"  [PASSED] Key '{key}' found in response with value: {response_data[key]}")

        # Step 7: Verify expected values
        print(f"\nStep 7: Verifying expected values in response")
        expected_values = {
            'id': 1,
            'price': 109.95,
            'category': "men's clothing"
        }

        for key, expected_value in expected_values.items():
            actual_value = response_data.get(key)
            assert actual_value == expected_value, \
                f"Expected {key}={expected_value}, but got {key}={actual_value}"
            print(f"  [PASSED] {key}: {actual_value} matches expected value: {expected_value}")

        print(f"\n{'='*70}")
        print("[SUCCESS] ALL TEST VALIDATIONS PASSED SUCCESSFULLY!")
        print(f"{'='*70}\n")

        # Close browser and context
        context.close()
        browser.close()


if __name__ == '__main__':
    # Run the test function directly
    test_fake_store_api_validation()

