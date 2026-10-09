from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ajax_content():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Нажимаем кнопку Start
    start_btn = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_btn.click()

    # Ждем появления текста и проверяем
    hello_element = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h4[text()='Hello World!']"))
    )
    assert hello_element.is_displayed(), (
        "Элемент с текстом 'Hello World!' не отображается"
    )
    assert hello_element.text == "Hello World!", (
        f"Текст элемента не 'Hello World!', а '{hello_element.text}'"
    )

    # Получаем текст через JavaScript и проверяем
    text_via_js = driver.execute_script(
        "return arguments[0].textContent;", hello_element
        )
    assert text_via_js == "Hello World!", (
        f"Текст через JavaScript не 'Hello World!', а '{text_via_js}'"
    )

    # Дополнительная проверка - элемент находится в DOM и видим
    assert hello_element.is_displayed(), "Элемент не видим на странице"

    driver.quit()
