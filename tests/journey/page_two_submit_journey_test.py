from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_test_journey_test import test_login

def test_page_two_submit_journey():
    driver = test_login()
    if driver is None:
        print("Login failed, cannot proceed with the test.")
        return

    try:
        # Step 1: Navigate to Page Two Digital Skills
        print("Navigating to Page Two Digital Skills...")
        driver.get("http://127.0.0.1:5000/PageTwoDigitalSkills")

        # Fill in question one
        print("Filling in question one...")
        driver.find_element(By.ID, "cybersecurity-answer").click()

        # Fill in question two
        print("Filling in question two...")
        driver.find_element(By.ID, "behavioral-interview-questions-answer").click()

        # Fill in question three
        print("Filling in question three...")
        driver.find_element(By.ID, "mentorship-programs-answer").click()

        # Fill in question four
        print("Filling in question four...")
        driver.find_element(By.ID, "promote-a-growth-mindset-answer").click()

        # Fill in question five
        print("Filling in question five...")
        driver.find_element(By.ID, "software-development-answer").click()

        # Fill in question six
        print("Filling in question six...")
        driver.find_element(By.ID, "leveraging-technology-answer").click()

        # Fill in question seven
        print("Filling in question seven...")
        driver.find_element(By.ID, "continuous-learning-answer").click()

        # Fill in question eight
        print("Filling in question eight...")
        driver.find_element(By.ID, "training-and-development-answer").click()

        # Fill in question nine
        print("Filling in question nine...")
        driver.find_element(By.ID, "pilot-testing-answer").click()

        # Fill in question ten
        print("Filling in question ten...")
        driver.find_element(By.ID, "interesting-projects-answer").click()

        # Click submit
        print("Clicking submit...")
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Save']"))
        )
        submit_button.click()
        
        # Wait for the alert and accept it
        print("Waiting for the alert and accepting it...")
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()

        # Click the 'Next' button
        print("Clicking Next...")
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and text()='Next']"))
        )
        next_button.click()

        # Wait for the page to reload after next navigation
        print("Waiting for the next page to load...")
        WebDriverWait(driver, 10).until(EC.url_contains("/PageThreeTechnologyAdoption"))
        
        print("Navigation to Page Three Technology Adoption completed successfully.")

    finally:
        driver.quit()