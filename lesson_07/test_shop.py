import pytest
from selenium import webdriver

from pageobject_shop import LoginPage, MainPage, CartPage, CheckoutPage


@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_shop(driver):
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

    assert "$58.29" in checkout_page.get_total(), "Итоговая сумма не $58.29"
