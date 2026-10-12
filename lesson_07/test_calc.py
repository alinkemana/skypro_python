import pytest
from selenium import webdriver

from pageobject_calc import SlowCalculatorPage


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_slow_calculator(driver):
    page = SlowCalculatorPage(driver)
    page.open()
    page.set_delay(45)

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    page.wait_for_result("15")
    assert page.get_result() == "15", "Результат калькулятора не 15"
