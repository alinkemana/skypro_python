import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


COOKIES_USER1 = [
    {
        "name": "SESSION",
        "value": "NmY5MDBkZTItYTA3MS00YjRhLWIxMjctMWVkYjE0ZjgwYzFl",
        "domain": ".gitflic.ru",
        "path": "/"
    }
]

COOKIES_USER2 = [
    {
        "name": "SESSION",
        "value": "OWQwMzZmODItYzI1Mi00ZDEzLThiMGUtZTdjZjBlMjBjMzY3",
        "domain": ".gitflic.ru",
        "path": "/"
    }
]

USER1_USERNAME = "foreignflor"
USER2_USERNAME = "grayjunior"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_session_storage_auth(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://gitflic.ru/")

    print("\n--- Входим как Пользователь 1 ---")

    for cookie in COOKIES_USER1:
        driver.add_cookie(cookie)

    driver.refresh()

    user1_url = f"https://gitflic.ru/user/{USER1_USERNAME}"
    driver.get(user1_url)

    wait.until(EC.url_contains(f"/user/{USER1_USERNAME}"))

    saved_url_user1 = driver.current_url

    assert "/login" not in saved_url_user1, (
        f"Cookie первого пользователя не сработала: {saved_url_user1}"
    )

    print(f"URL Пользователя 1: {saved_url_user1}")

    driver.delete_all_cookies()
    print("Cookie очищены (разлогин)")

    print("\n--- Входим как Пользователь 2 ---")

    for cookie in COOKIES_USER2:
        driver.add_cookie(cookie)

    driver.refresh()

    user2_url = f"https://gitflic.ru/user/{USER2_USERNAME}"
    driver.get(user2_url)

    wait.until(EC.url_contains(f"/user/{USER2_USERNAME}"))

    saved_url_user2 = driver.current_url

    assert "/login" not in saved_url_user2, (
        f"Cookie второго пользователя не сработала: {saved_url_user2}"
    )

    print(f"URL Пользователя 2: {saved_url_user2}")

    assert saved_url_user1 != saved_url_user2, (
        f"URL профилей должны различаться!\n"
        f"Пользователь 1: {saved_url_user1}\n"
        f"Пользователь 2: {saved_url_user2}"
    )
    print("\n✅ Тест пройден: URL профилей различаются.")
