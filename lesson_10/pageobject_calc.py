from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class SlowCalculatorPage:
    DELAY_FIELD = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(
        self,
        driver,
        url="https://bonigarcia.dev/selenium-webdriver-"
        "java/slow-calculator.html",
    ):
        """
        Конструктор класса SlowCalculatorPage:.

        :param driver: WebDriver — объект драйвера Selenium.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        :param url: str — адрес страницы калькулятора.
        :type url: str
        :return: None
        :rtype: None
        """
        self.driver = driver
        self.url = url
        # 50 секунд, потому что задержка 45 + запас на отрисовку
        self.wait = WebDriverWait(driver, 50)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.

        :return: None
        :rtype: None
        """
        self.driver.get(self.url)

    @allure.step("Установка задержки {seconds} секунд")
    def set_delay(self, seconds):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param seconds: int — время задержки в секундах.
        :type seconds: int | str
        :return: None
        :rtype: None
        """
        field = self.wait.until(
            EC.presence_of_element_located(self.DELAY_FIELD)
        )
        field.clear()
        field.send_keys(str(seconds))

    @allure.step("Нажатие кнопки '{text}'")
    def click_button(self, text):
        """
        Нажимает на кнопку калькулятора.

        :param text: str — текст на кнопке, которую нужно нажать.
        :type text: str
        :return: None
        :rtype: None
        """
        locator = (By.XPATH, f"//span[normalize-space()='{text}']")
        button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    @allure.step("Ожидание результата '{expected}'")
    def wait_for_result(self, expected):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param expected: str — ожидаемый результат.
        :type expected: str
        :return: None
        :rtype: None
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: текст результата на экране калькулятора.
        :rtype: str
        """
        screen = self.wait.until(
            EC.presence_of_element_located(self.SCREEN)
        )
        return screen.text
