import allure
import pytest
from selenium import webdriver
from pageobject_shop import LoginPage, MainPage, CartPage, CheckoutPage


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.

    :return: WebDriver — объект драйвера.
    :rtype: selenium.webdriver.remote.webdriver.WebDriver
    """
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


@allure.feature("Магазин")
@allure.title("Добавление товаров в корзину и оформление заказа")
@allure.description("Тест проходит полный путь пользователя: авторизация,"
                    "добавление трех товаров, заполнение формы"
                    "и проверка итоговой стоимости")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
    Тест проверяет полный сценарий покупки товаров в магазине.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: None
    :rtype: None
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_login("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login()

    main_page = MainPage(driver)
    main_page.add_to_cart("sauce-labs-backpack")
    main_page.add_to_cart("sauce-labs-bolt-t-shirt")
    main_page.add_to_cart("sauce-labs-onesie")
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Alina", "Nasyrova", "123456")
    checkout_page.click_continue()

    with allure.step("Проверка, что итоговая сумма равна $58.29"):
        total = checkout_page.get_total()
        assert "$58.29" in total, "Итоговая сумма не $58.29"
