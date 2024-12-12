from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_test_journey_test import test_login

def test_login_to_page_one():
    driver = test_login()
    if driver is None:
        print("Login failed, cannot proceed with the test.")
        return

    try:
        driver.get("http://127.0.0.1:5000/")

        # Click the 'Start' button
        print("Clicking Start...")
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
        )
        next_button.click()

        # Wait for the page to reload after navigation
        print("Waiting for the next page to load...")
        WebDriverWait(driver, 10).until(EC.url_contains("/PageOneDigitalStrategy"))

        print("Navigation to Page One Digital Strategy completed successfully.")

    finally:
        driver.quit()