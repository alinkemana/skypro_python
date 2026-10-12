from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(
        self,
        driver,
        url="https://www.saucedemo.com/",
    ):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открыть страницу магазина."""
        self.driver.get(self.url)

    def fill_login(self, username):
        """Ввести логин."""
        field = self.wait.until(
           EC.presence_of_element_located(self.USERNAME)
        )
        field.clear()
        field.send_keys(username)

    def fill_password(self, password):
        """Ввести пароль."""
        field = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD)
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        """Нажать кнопку входа."""
        button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        button.click()


class MainPage:
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_id):
        """добавить в корзину."""
        locator = (By.ID, f"add-to-cart-{product_id}")
        button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def go_to_cart(self):
        """перейти в корзину."""
        cart = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart.click()


class CartPage:
    CHECKOUT = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        """нажать на кнопку Checkout."""
        button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT)
        )
        button.click()

    def check_cart_items(self):
        """проверить список названий товаров в корзине."""
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
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
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

    def click_continue(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE)
        )
        button.click()

    def get_total(self):
        """Вернуть текст итоговой стоимости."""
        total = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL)
        )
        return total.text
