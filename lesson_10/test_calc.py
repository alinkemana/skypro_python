import allure
import pytest
from selenium import webdriver
from pageobject_calc import SlowCalculatorPage


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.

    :return: WebDriver — объект драйвера.
    :rtype: selenium.webdriver.remote.webdriver.WebDriver
    """
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@allure.feature("Калькулятор")
@allure.title("Проверка сложения: 7 + 8 = 15")
@allure.description("Тест проверяет корректность выполнения операции сложения"
                    "на калькуляторе.")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver):
    """
    Тест проверяет работу калькулятора.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: None
    :rtype: None
    """
    page = SlowCalculatorPage(driver)
    page.open()
    page.set_delay(45)

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    page.wait_for_result("15")

    with allure.step("Проверка результата на экране"):
        assert page.get_result() == "15", "Результат калькулятора не 15"
