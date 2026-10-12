from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    DELAY_FIELD = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(
        self,
        driver,
        url="https://bonigarcia.dev/selenium-webdriver-"
        "java/slow-calculator.html",
    ):
        self.driver = driver
        self.url = url
        # 50 секунд, потому что задержка 45 + запас на отрисовку
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        """Открыть страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, seconds):
        """Ввести значение задержки в поле #delay."""
        field = self.wait.until(
            EC.presence_of_element_located(self.DELAY_FIELD)
        )
        field.clear()
        field.send_keys(str(seconds))

    def click_button(self, text):
        """Нажать кнопку калькулятора по её тексту."""
        locator = (By.XPATH, f"//span[normalize-space()='{text}']")
        button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def wait_for_result(self, expected):
        """Ждать, пока в окне калькулятора появится нужный текст."""
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )

    def get_result(self):
        """Вернуть текст из окна результата."""
        screen = self.wait.until(
            EC.presence_of_element_located(self.SCREEN)
        )
        return screen.text
