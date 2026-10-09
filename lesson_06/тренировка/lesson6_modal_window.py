from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_modal_window():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/entry_ad")

    # Ждем появления модального окна
    modal = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal"))
    )
    assert modal.is_displayed(), "Модальное окно не отобразилось"

    # Проверяем текст в модальном окне
    modal_text = modal.find_element(By.CLASS_NAME, "modal-title")
    assert "This is a modal window" in modal_text.text, (
        "Текст модального окна не соответствует ожидаемому"
    )

    # Закрываем модальное окно
    close_btn = modal.find_element(By.XPATH, ".//p[text()='Close']")
    close_btn.click()

    # Ждем исчезновения модального окна и проверяем
    wait.until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "modal"))
    )
    modals_after_close = driver.find_elements(By.CLASS_NAME, "modal")
    assert len(modals_after_close) == (
        0 or not modals_after_close[0].is_displayed(),
    )
    (
        "Модальное окно не закрылось"
    )
    # Проверяем, что основной контент страницы виден
    content = driver.find_element(By.ID, "content")
    assert content.is_displayed(), "Основной контент страницы не виден"

    driver.quit()
