from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObjectKinopoisk:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.kinopoisk.ru/"

        # Локатор строки поиска
        self.search_input = (
            By.CSS_SELECTOR, 'input.kinopoisk-header-search-form-input__input'
        )

    def open(self):
        """Открывает главную страницу Кинопоиска"""
        self.driver.get(self.url)

    def search_for(self, query: str):
        """Вводит текст в поиск и нажимает Enter"""
        search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_input)
        )
        search_field.clear()
        search_field.send_keys(query)
        search_field.send_keys(Keys.RETURN)

    def is_movie_found(self, movie_name: str) -> bool:
        """Ищет фильм на странице результатов поиска."""
        try:
            # Ищем ЛЮБОЙ элемент на странице, внутри которого есть текст
            locator = (By.XPATH, f'//*[contains(text(), "{movie_name}")]')
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def open_movie_card(self, movie_name: str):
        """Кликает по информации о фильме в результатах поиска, чтобы перейти в карточку фильма."""
        # Ищем ссылку с названием фильма и ждем, пока она станет кликабельной
        locator = (By.CSS_SELECTOR, 'div[data-test-id="movie-list-item"]')
        movie_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        assert movie_name in movie_link.text, f"В первой карточке нет фильма {movie_name}"
        movie_link.click()
