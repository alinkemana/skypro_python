import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_dynamic_loading(driver):
    wait = WebDriverWait(driver, 15)

    # 1. Открыть страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найти и нажать кнопку Start (по CSS-селектору)
    start_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    start_btn.click()

    # 3. Дождаться появления текста "Hello World!"
    hello_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # 4. Сделать скриншот
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot("screenshots/full_screen.png")

    # 5. Проверить, что текст равен "Hello World!"
    assert hello_element.text == "Hello World!", (
        f"Ожидался текст 'Hello World!', получен '{hello_element.text}'"
    )
