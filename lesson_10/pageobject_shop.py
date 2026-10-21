from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(
        self,
        driver,
        url="https://www.saucedemo.com/",
    ):
        """
        Конструктор класса LoginPage.

        :param driver: WebDriver — объект драйвера Selenium.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        :param url: str — адрес страницы магазина.
        :type url: str
        :return: None
        :rtype: None
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы магазина")
    def open(self):
        """
        Открывает страницу магазина.

        :return: None
        :rtype: None
        """
        self.driver.get(self.url)

    @allure.step("Ввод логина {username}")
    def fill_login(self, username):
        """
        Ввести логин.

        :param username: str — текст, который нужно ввести.
        :type username: int | str
        :return: None
        :rtype: None
        """
        field = self.wait.until(
           EC.presence_of_element_located(self.USERNAME)
        )
        field.clear()
        field.send_keys(username)

    @allure.step("Ввод пароля")
    def fill_password(self, password):
        """
        Ввести пароль.

        :param password: str — текст, который нужно ввести.
        :type password: int | str
        :return: None
        :rtype: None
        """
        field = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD)
        )
        field.clear()
        field.send_keys(password)

    @allure.step("Нажатие кнопки входа")
    def click_login(self):
        """
        Нажать на кнопку входа.

        :return: None
        :rtype: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        button.click()


class MainPage:
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        :return: None
        :rtype: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товара {product_id} в корзину")
    def add_to_cart(self, product_id):
        """
        Добавить в корзину.

        :param product_id: int
        :type product_id: int
        :return: None
        :rtype: None
        """
        locator = (By.ID, f"add-to-cart-{product_id}")
        button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Перейти в корзину.

        :return: None
        :rtype: None
        """
        cart = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart.click()


class CartPage:
    CHECKOUT = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        :return: None
        :rtype: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажатие на кнопку Checkout")
    def click_checkout(self):
        """
        Нажать на кнопку Checkout.

        :return: None
        :rtype: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT)
        )
        button.click()

    @allure.step("Проверка списка названий товаров в корзине")
    def check_cart_items(self):
        """
        Проверить список названий товаров в корзине.

        :return: список названий товаров.
        :rtype: list[str]
        """
        self.wait.until(
            EC.presence_of_element_located(self.CART_ITEM)
        )
        items = self.driver.find_elements(*self.CART_ITEM)
        return [item.text for item in items]


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        :return: None
        :rtype: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнение данных: {first_name}, {last_name}, {postal_code}")
    def fill_form(self, first_name, last_name, postal_code):
        """
        Заполнить данные: имя, фамилия, почтовый код.

        :param first_name: str — имя.
        :param last_name: str — фамилия.
        :param postal_code: str — индекс.
        :type first_name: int | str
        :type last_name: int | str
        :type postal_code: int | str
        :return: None
        :rtype: None
        """
        first = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME)
        )
        first.clear()
        first.send_keys(first_name)

        last = self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME)
        )
        last.clear()
        last.send_keys(last_name)

        code = self.wait.until(
            EC.presence_of_element_located(self.POSTAL_CODE)
        )
        code.clear()
        code.send_keys(postal_code)

    @allure.step("Нажатие кнопки continue")
    def click_continue(self):
        """
        Нажать на кнопку continue.

        :return: None
        :rtype: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE)
        )
        button.click()

    @allure.step("Возврат итоговой стоимости")
    def get_total(self):
        """
        Вернуть текст итоговой стоимости.

        :return: text
        :rtype: str
        """
        total = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL)
        )
        return total.text
