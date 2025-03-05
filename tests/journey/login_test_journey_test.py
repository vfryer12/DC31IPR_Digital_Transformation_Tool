from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def test_login():
    # Start a new browser session 
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the login page
        driver.get("http://127.0.0.1:5000/login")

        # Fill in login form
        driver.find_element(By.ID, "username").send_keys("victoria")
        driver.find_element(By.ID, "password").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Wait for the page to reload after login
        WebDriverWait(driver, 10).until(EC.url_changes("http://127.0.0.1:5000/login"))

        # Return the driver if login is successful
        return driver
    except Exception as e:
        logging.debug(f"Login failed: {e}")
        driver.quit()
        return None
