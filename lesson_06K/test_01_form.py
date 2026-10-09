from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    driver = webdriver.Safari()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        wait.until(
            EC.visibility_of_element_located((By.NAME, "first-name"))
        ).send_keys("Иван")

        driver.find_element(By.NAME, "last-name").send_keys("Петров")

        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")

        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")

        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")

        # zip-code оставляем пустым

        driver.find_element(By.NAME, "city").send_keys("Москва")

        driver.find_element(By.NAME, "country").send_keys("Россия")

        driver.find_element(By.NAME, "job-position").send_keys("QA")

        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit'"
                 "and normalize-space()='Submit']")
            )
        )
        driver.execute_script("arguments[0].click();", submit_button)

        zip_code = wait.until(
           EC.visibility_of_element_located((By.ID, "zip-code"))
        )
        assert "alert-danger" in zip_code.get_attribute("class"), (
            "Поле Zip code должно быть подсвечено красным"
        )

        green_fields = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company",
        ]
        for field_id in green_fields:
            element = driver.find_element(By.ID, field_id)
        assert "alert-success" in element.get_attribute("class"), (
            f"Поле {field_id} должно быть подсвечено зелёным"
        )

    finally:
        driver.quit()
