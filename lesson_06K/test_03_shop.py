from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        driver.find_element(
            By.CSS_SELECTOR, "[data-test='shopping-cart-link']"
        ).click()

        driver.find_element(By.ID, "checkout").click()

        wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Alina")

        driver.find_element(By.ID, "last-name").send_keys("Nasyrova")

        driver.find_element(By.ID, "postal-code").send_keys("Krasina 19/1-92")

        driver.find_element(By.ID, "continue").click()

        total_element = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = total_element.text

        assert "$58.29" in total_text, (
            f"Ожидалась сумма $58.29, а получено: {total_text}"
        )

    finally:
        driver.quit()
