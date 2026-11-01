import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.page_object_kinopoisk import PageObjectKinopoisk


@pytest.fixture()
def driver() -> webdriver.Chrome:
    """
    Фикстура для инициализации и завершения работы драйвера.

    :return: WebDriver — объект драйвера.
    :rtype: selenium.webdriver.remote.webdriver.WebDriver
    """
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.mark.ui
@allure.feature("Кинопоиск")
@allure.story("Поиск")
@allure.title("Поиск фильма по названию")
@allure.description("Тест проверяет, что при поиске открывается страница с результатами")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_movie_by_name(driver: webdriver.Chrome) -> None:
    """
    Тест проверяет поиск фильма по его полному названию.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: None
    :rtype: None
    """

    page = PageObjectKinopoisk(driver)

    with allure.step("Открыть главную страницу Кинопоиска"):
        page.open()

    with allure.step("Ввести название фильма и нажать Enter"):
        page.search_for("Начало")

    with allure.step("Проверка того, что фильм 'Начало' отображается в результатах поиска"):
        # 1. Вызываем метод и сохраняем результат (True или False) в переменную
        is_found = page.is_movie_found("Начало")

        # 2. Делаем проверку: если is_found не равен True, тест упадет с ошибкой
        assert is_found is True, "Фильм 'Начало' не найден на странице результатов!"


@pytest.mark.ui
@allure.feature("Кинопоиск")
@allure.story("Поиск")
@allure.title("Поиск фильма по частичному названию")
@allure.description("Тест проверяет, что при поиске открывается страница с результатами")
@allure.severity(allure.severity_level.NORMAL)
def test_search_movie_by_partial_name(driver: webdriver.Chrome) -> None:
    """
    Тест проверяет поиск фильма по его частичному названию.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: None
    :rtype: None
    """

    page = PageObjectKinopoisk(driver)

    with allure.step("Открыть главную страницу Кинопоиска"):
        page.open()

    with allure.step("Ввести название фильма частично и нажать Enter"):
        page.search_for("Нача")

    with allure.step("Проверка того, что фильм 'Начало' отображается в результатах поиска"):
        # 1. Вызываем метод и сохраняем результат (True или False) в переменную
        is_found = page.is_movie_found("Начало")

        # 2. Делаем проверку: если is_found не равен True, тест упадет с ошибкой
        assert is_found is True, "Фильм 'Начало' не найден на странице результатов!"


@pytest.mark.ui
@allure.feature("Кинопоиск")
@allure.story("Карточка фильма")
@allure.title("Переход в карточку фильма из поиска")
@allure.description("Тест проверяет, что при переходе в карточку фильма отображается вся информация о фильме")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_movie_info(driver: webdriver.Chrome) -> None:
    """
    Тест проверяет переход в карточку фильма из поиска.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: None
    :rtype: None
    """

    page = PageObjectKinopoisk(driver)

    with allure.step("Открыть главную страницу Кинопоиска"):
        page.open()

    with allure.step("Ввести название фильма и нажать Enter"):
        page.search_for("Начало")

    with allure.step("Нажать на информацию о фильме, чтобы перейти в его карточку"):
        page.open_movie_card("Начало")

    with allure.step("Проверка, что открылась страница фильма"):
        # 1. Ждем, пока URL изменится на страницу фильма (там будет /film/)
        WebDriverWait(driver, 10).until(
            EC.url_contains("/film/")
        )

        # 2. Дополнительная проверка: ищем заголовок (h1) с названием фильма
        movie_title_locator = (By.TAG_NAME, "h1")
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(movie_title_locator)
        )

        # Проверяем, что в заголовке написано "Начало"
        assert "Начало" in title_element.text, f"Ожидали фильм 'Начало', но нашли: {title_element.text}"


@pytest.mark.ui
@allure.feature("Кинопоиск")
@allure.story("Карточка фильма")
@allure.title("Просмотр блока с актерами в карточке фильма")
@allure.description("Тест проверяет, что при переходе в карточку фильма отображается блок об актерах")
@allure.severity(allure.severity_level.NORMAL)
def test_check_actors_block(driver: webdriver.Chrome) -> None:
    """
    Тест проверяет, что при переходе в карточку фильма отображается блок об актерах.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: None
    :rtype: None
    """

    page = PageObjectKinopoisk(driver)

    with allure.step("Открыть главную страницу Кинопоиска"):
        page.open()

    with allure.step("Ввести название фильма и нажать Enter"):
        page.search_for("Начало")

    with allure.step("Нажать на информацию о фильме, чтобы перейти в его карточку"):
        page.open_movie_card("Начало")

    with allure.step("Проверка, что открылась страница фильма"):
        # Ждем, пока URL изменится на страницу фильма (там будет /film/)
        WebDriverWait(driver, 10).until(
            EC.url_contains("/film/")
        )

        # Дополнительная проверка: ищем заголовок (h1) с названием фильма
        movie_title_locator = (By.TAG_NAME, "h1")
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(movie_title_locator)
        )

        # Проверяем, что в заголовке написано "Начало"
        assert "Начало" in title_element.text, f"Ожидали фильм 'Начало', но нашли: {title_element.text}"

        # Ищем заголовок блока об актерах "В главных ролях"
        actor_title_locator = (By.XPATH, '//*[contains(text(), "В главных ролях")]')
        actor_title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(actor_title_locator)
        )

        # Проверяем, что в блок об актерах просматривается
        assert "В главных ролях" in actor_title_element.text, f"Ожидали текст 'В главных ролях', но нашли: {actor_title_element.text}"


@pytest.mark.ui
@allure.feature("Кинопоиск")
@allure.story("Фильтрация")
@allure.title("Фильтрация фильмов по жанру 'комедия'")
@allure.description("Тест проверяет, что при выборе жанра 'Комедия' открывается страница с результатами поиска фильмов по указанному жанру")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_by_filter(driver: webdriver.Chrome) -> None:
    """
    Тест проверяет, что при выборе жанра 'Комедия' открывается страница с результатами поиска фильмов по указанному жанру

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: None
    :rtype: None
    """

    page = PageObjectKinopoisk(driver)

    with allure.step("Открыть главную страницу Кинопоиска"):
        page.open()

    with allure.step("Нажать на иконку фильтра для перехода на расширенный поиск"):
        filter_locator = (By.CSS_SELECTOR, 'svg[class*="advancedSearchIcon"]')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(filter_locator)
        ).click()

    with allure.step("Дождаться загрузки формы расширенного поиска, URL страницы изменится "
                     "и будет содержать /s/ (это страница расширенного поиска)."):
        WebDriverWait(driver, 10).until(EC.url_contains("/s/"))

    with allure.step("Прокрутить страницу вниз до блока 'жанр'"):
        genre_element = driver.find_element(
            By.XPATH, '//b[@class="txt_7" and normalize-space()="+ жанр:"]'
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", genre_element)

    with allure.step("Выбрать жанр 'комедия'"):
        # находим окошко со списком жанров
        select_locator = (By.XPATH, '//select[@id="m_act[genre]"]')

        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(select_locator)
        )
        # Прокручиваем до него
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_element)

        # Инициализируем Select и выбираем по тексту
        genre_select = Select(select_element)
        genre_select.select_by_visible_text("комедия")

    with allure.step("Нажать кнопку 'поиск'"):
        search_button_locator = (By.CSS_SELECTOR, 'input[type="button"][value="поиск"]')

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(search_button_locator)
        ).click()

    with allure.step("Проверить, что открылась страница с результатами по жанру 'комедия'"):
        # 1. Ждем появления результатов с карточками фильмов
        result_cardfilm_locator = (By.CSS_SELECTOR, 'div.element')
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(result_cardfilm_locator)
        )

        # 2. Ищем подтверждение жанра среди блоков фильмов
        blocks = driver.find_elements(*result_cardfilm_locator)
        assert len(blocks) > 0, "На странице не найдено ни одного фильма!"

        found_comedy = False
        # Проверяем первые 10 блоков (чтобы тест не работал слишком долго)
        for block in blocks[:10]:
            # берем текст из карточки и переводим в нижний регистр (чтобы "Комедия" и "комедия" считались одинаковыми)
            block_text = block.text.lower()

            # Если находим "комедия", фиксируем успех
            if "комедия" in block_text:
                found_comedy = True
                break

        # Если цикл закончился, а комедии нет - тест упадет с ошибкой
        assert found_comedy, "Среди первых 10 фильмов не найдено ни одного с жанром 'комедия'!"


@pytest.mark.ui
@allure.feature("Кинопоиск")
@allure.story("Фильтрация")
@allure.title("Фильтрация фильмов по двум жанрам (комедия и приключения)")
@allure.description("Тест проверяет, что при выборе двух жанров открывается страница с результатами поиска по этим жанрам")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_by_two_genres(driver):
    """
    Тест проверяет, что при выборе двух жанров открывается страница с результатами поиска по этим жанрам

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: None
    :rtype: None
    """

    page = PageObjectKinopoisk(driver)

    with allure.step("Открыть главную страницу Кинопоиска"):
        page.open()

    with allure.step("Нажать на иконку фильтра для перехода на расширенный поиск"):
        filter_locator = (By.CSS_SELECTOR, 'svg[class*="advancedSearchIcon"]')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(filter_locator)
        ).click()

    with allure.step("Дождаться загрузки формы расширенного поиска"):
        WebDriverWait(driver, 10).until(EC.url_contains("/s/"))

    with allure.step("Прокрутить страницу вниз до блока 'жанр'"):
        genre_element = driver.find_element(
            By.XPATH, '//b[@class="txt_7" and normalize-space()="+ жанр:"]'
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", genre_element)

    with allure.step("Выбрать жанры 'комедия' и 'приключения'"):
        select_locator = (By.XPATH, '//select[@id="m_act[genre]"]')

        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(select_locator)
        )

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_element)

        genre_select = Select(select_element)

        # Выбираем первый жанр
        genre_select.select_by_visible_text("комедия")
        # Выбираем второй жанр (класс Select сам добавит его к выбору, так как список - multiple)
        genre_select.select_by_visible_text("приключения")

    with allure.step("Нажать кнопку 'поиск'"):
        search_button_locator = (By.CSS_SELECTOR, 'input[type="button"][value="поиск"]')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(search_button_locator)
        ).click()

    with allure.step("Проверить, что открылась страница с результатами по выбранным жанрам"):
        result_cardfilm_locator = (By.CSS_SELECTOR, 'div.element')
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(result_cardfilm_locator)
        )

        blocks = driver.find_elements(*result_cardfilm_locator)
        assert len(blocks) > 0, "На странице не найдено ни одного фильма!"

        # Проверяем, что среди фильмов есть представители выбранных жанров
        has_comedy = False
        has_adventure = False

        # Проверяем первые 15 блоков, чтобы наверняка найти оба жанра
        for block in blocks[:15]:
            block_text = block.text.lower()

            if "комедия" in block_text:
                has_comedy = True
            if "приключения" in block_text:
                has_adventure = True

            # Если нашли оба, дальше можно не проверять
            if has_comedy and has_adventure:
                break

        # Проверяем, что на странице есть фильмы хотя бы с одним из жанров
        assert has_comedy or has_adventure, "Среди первых 15 фильмов не найдено ни одного с жанром 'комедия' или 'приключения'!"
