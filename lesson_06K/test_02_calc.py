from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 50)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

        delay_field = driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys("45")

        driver.find_element(
            By.XPATH, "//span[normalize-space()='7']"
            ).click()

        driver.find_element(
            By.XPATH,
            "//span[@class='operator btn btn-outline-success'"
            "and normalize-space()='+']"
        ).click()

        driver.find_element(
            By.XPATH, "//span[normalize-space()='8']"
        ).click()

        driver.find_element(
            By.XPATH,
            "//span[@class='btn btn-outline-warning'"
            "and normalize-space()='=']"
        ).click()

        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )

    finally:
        driver.quit()
