from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_registration_to_login_journey():
    # Start a new browser session
    driver = webdriver.Chrome()

    try:
        # Step 1: Navigate to the registration page
        driver.get("http://127.0.0.1:5000/registration")
        
        # Fill in the registration form
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "fname").send_keys("Test")
        driver.find_element(By.ID, "lname").send_keys("User")
        driver.find_element(By.ID, "email").send_keys("testuser@example.com")
        driver.find_element(By.ID, "pwd").send_keys("password123")
        driver.find_element(By.ID, "cpwd").send_keys("password123")
        
        # Submit the registration form
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        
        # Wait for the page to reload after form submission
        time.sleep(2)
        
        # Navigate to the login page
        driver.get("http://127.0.0.1:5000/login")
        
        # Fill in login form
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("password123")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Wait for the page to reload after login
        time.sleep(2)

    finally:
        driver.quit()
