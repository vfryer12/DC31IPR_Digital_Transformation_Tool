from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_test_journey_test import test_login
import time

def test_page_one_to_page_two(): 
    # Start a new browser session 
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    # Use incognito mode to start with a clean session
    driver = webdriver.Chrome(options=options)

    try:

        # Login in
        test_login()

        # Step 1: Navigate to page one
        driver.get("http://127.0.0.1:5000/PageOneDigitalStrategy")

        # Fill in question one
        driver.find_element(By.ID, "no-plan").click()

        # Fill in question two
        # Locate the dropdown element
        dropdown = Select(driver.find_element(By.ID, "question-two-dropdown"))
        # Select the option by visible text
        dropdown.select_by_visible_text("Chief Information Officer (CIO)")

        # Fill in question three
        driver.find_element(By.ID, "question-three-monthly").click()

        # Fill in question four
        driver.find_element(By.ID, "customer-engagement-answer").click()

        # Fill in question five
        driver.find_element(By.ID, "digital-investments-answer").click()

        # Fill in question six
        driver.find_element(By.ID, "engagement-answer").click()

        # Fill in question seven
        driver.find_element(By.ID, "resistance-to-change-answer").click()

        # Fill in question eight
        driver.find_element(By.ID, "documentation-answer").click()

        # Fill in question nine
        driver.find_element(By.ID, "risk-assessment-answer").click()

        # Fill in question ten
        driver.find_element(By.ID, "customer-feedback-answer").click()

        # Click submit
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Save']")) )
        submit_button.click()
        # Wait for the page after submit
        time.sleep(2)

        # Wait for the alert and accept it
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()

        time.sleep(2)

        # # Click Next
        # # Click the 'Next' button
        # next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and text()='Next']")) )

        # #next_button = driver.find_element(By.XPATH, "//button[@type='button' and text()='Next']")
        # next_button.click()

        # Wait for the page to reload after next navigation
        time.sleep(2)

    finally:
        driver.quit()
        