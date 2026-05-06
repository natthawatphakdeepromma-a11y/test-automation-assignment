import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

LOGIN_URL = "http://the-internet.herokuapp.com/login"
VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def get_flash_message(driver):
    # Helper: wait for and return the flash alert message text.
    wait = WebDriverWait(driver, 10)
    flash = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    return flash.text.strip()

# Test Case 1: Login success
def test_login_success(driver):
    # Log in with the correct credentials, then logout.
    driver.get(LOGIN_URL)
    assert "login" in driver.current_url, "Login page should be displayed"

    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = get_flash_message(driver)
    assert "You logged into a secure area!" in message, (
        f"Expected success message, got: {message}"
    )
    driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()

    logout_message = get_flash_message(driver)
    assert "You logged out of the secure area!" in logout_message, (
        f"Expected logout message, got: {logout_message}"
    )
    print("Test Case 1 PASSED: Login success")

# Test Case 2: Login failed – Password incorrect
def test_login_failed_wrong_password(driver):
    #If the password is incorrect, an error should appear.
    driver.get(LOGIN_URL)
    assert "login" in driver.current_url, "Login page should be displayed"
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("Password!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = get_flash_message(driver)
    assert "Your password is invalid!" in message, (
        f"Expected invalid password message, got: {message}"
    )
    print("Test Case 2 PASSED: Login failed – wrong password")

# Test Case 3: Login failed – Username not found
def test_login_failed_username_not_found(driver):
    # Entering a username that doesn't exist in the system should result in an error.
    driver.get(LOGIN_URL)
    assert "login" in driver.current_url, "Login page should be displayed"

    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys("tomholland")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("Password!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = get_flash_message(driver)
    assert "Your username is invalid!" in message, (
        f"Expected invalid username message, got: {message}"
    )
    print(" Test Case 3 PASSED: Login failed – username not found")

