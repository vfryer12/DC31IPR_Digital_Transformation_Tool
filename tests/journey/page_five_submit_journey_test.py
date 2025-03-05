from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_test_journey_test import test_login
import logging

def test_page_five_submit_journey():
    driver = test_login()
    if driver is None:
        logging.debug("Login failed, cannot proceed with the test.")
        return

    try:
        # Step 1: Navigate to Page Five Digital Marketing
        logging.debug("Navigating to Page Five Marketing")
        driver.get("http://127.0.0.1:5000/PageFiveDigitalMarketing")

        # Fill in question one
        logging.debug("Filling in question one")
        driver.find_element(By.ID, "influencer-marketing-answer").click()

        # Fill in question two
        logging.debug("Filling in question two")
        driver.find_element(By.ID, "customer-acquisition-cost-answer").click()

        # Fill in question three
        logging.debug("Filling in question three")
        driver.find_element(By.ID, "investing-in-content-marketing-answer").click()

        # Fill in question four
        logging.debug("Filling in question four")
        driver.find_element(By.ID, "expanding-video-marketing-answer").click()

        # Fill in question five
        logging.debug("Filling in question five")
        driver.find_element(By.ID, "technical-seo-answer").click()

        # Fill in question six
        logging.debug("Filling in question six")
        driver.find_element(By.ID, "content-promotion-answer").click()

        # Fill in question seven
        logging.debug("Filling in question seven")
        driver.find_element(By.ID, "abandoned-cart-emails-answer").click()

        # Fill in question eight
        logging.debug("Filling in question eight")
        driver.find_element(By.ID, "email-newsletters-answer").click()

        # Fill in question nine
        logging.debug("Filling in question nine")
        driver.find_element(By.ID, "building-long-term-relationships-answer").click()

        # Fill in question ten
        logging.debug("Filling in question ten")
        driver.find_element(By.ID, "educational-content-answer").click()

        # Click submit
        logging.debug("Clicking submit")
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Save']"))
        )
        submit_button.click()
        
        # Wait for the alert and accept it
        logging.debug("Waiting for the alert and accepting it")
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()

        # Click the Next button
        logging.debug("Clicking Next")
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and text()='Next']"))
        )
        next_button.click()

        # Wait for the page to reload after next navigation
        logging.debug("Waiting for the next page to load")
        WebDriverWait(driver, 10).until(EC.url_contains("/SubmitAssessmentPage"))
        
        logging.debug("Navigation to Page Submit Assessment completed successfully.")

    finally:
        driver.quit()