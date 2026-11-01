import requests
import pytest
from config.settings import settings


# --- ТЕСТ 1: ПОИСК ФИЛЬМА ПО НАЗВАНИЮ ---
@pytest.mark.api
def test_search_movie():
    # 1. Формируем адрес запроса
    url = f"{settings.BASE_URL}/v1.5/movie/search"

    # 2. Формируем заголовки
    headers = {
        "X-API-KEY": settings.API_TOKEN,
        "accept": "application/json"
    }

    # 3. Формируем параметры (что ищем)
    params = {
        "query": "Начало"
    }

    # 4. Отправляем запрос
    response = requests.get(url, headers=headers, params=params)

    # 5. Проверяем, что статус-код 200
    assert response.status_code == 200, f"Ожидали 200, но получили {response.status_code}"

    # 6. Проверяем, что в ответе есть список фильмов (docs)
    data = response.json()
    assert "docs" in data, "В ответе нет ключа 'docs'"
    assert len(data["docs"]) > 0, "Список фильмов пуст"

    print(f"Тест пройден! Найдено фильмов: {len(data['docs'])}")


# --- ТЕСТ 2: ПОЛУЧЕНИЕ ФИЛЬМА ПО ID ---
@pytest.mark.api
def test_search_movie_by_id():
    # 1. Формируем адрес запроса
    url = f"{settings.BASE_URL}/v1.5/movie/447301"

    # 2. Формируем заголовки
    headers = {
        "X-API-KEY": settings.API_TOKEN,
        "accept": "application/json"
    }

    # 3. Отправляем запрос
    response = requests.get(url, headers=headers)

    # 4. Проверяем, что статус-код 200
    assert response.status_code == 200, f"Ожидали 200, но получили {response.status_code}"

    # 5. Проверяем, что в ответе есть фильм с указанным id
    data = response.json()
    assert data["id"] == 447301, f"Ожидали ID 447301, но получили {data['id']}"

    print("Тест пройден! Найден фильм с указанным id")


# --- ТЕСТ 3: ФИЛЬТРАЦИЯ ПО ЖАНРУ ---
@pytest.mark.api
def test_get_movie_genre():
    # 1. Формируем адрес запроса
    url = f"{settings.BASE_URL}/v1.5/movie"

    # 2. Формируем заголовки
    headers = {
        "X-API-KEY": settings.API_TOKEN,
        "accept": "application/json"
    }

    # 3. Формируем параметры (что ищем)
    params = {
        "genres.name": "комедия"
    }

    # 4. Отправляем запрос
    response = requests.get(url, headers=headers, params=params)

    # 5. Проверяем, что статус-код 200
    assert response.status_code == 200, f"Ожидали 200, но получили {response.status_code}"

    # 6. Проверяем, что в ответе есть список фильмов (docs)
    data = response.json()
    assert "docs" in data, "В ответе нет ключа 'docs'"
    assert len(data["docs"]) > 0, "Список фильмов пуст"

    # (Опционально) Проверяем, что первый фильм в списке действительно комедия
    first_movie_genres = data["docs"][0]["genres"]
    genre_names = [genre["name"] for genre in first_movie_genres]
    assert "комедия" in genre_names, "Первый фильм в списке не является комедией"

    print(f"Тест пройден! Найдено фильмов: {len(data['docs'])}")


# --- ТЕСТ 4: ПОЛУЧЕНИЕ СЛУЧАЙНОГО ФИЛЬМА ---
@pytest.mark.api
def test_get_movie_random():
    # 1. Формируем адрес запроса
    url = f"{settings.BASE_URL}/v1.5/movie/random"

    # 2. Формируем заголовки
    headers = {
        "X-API-KEY": settings.API_TOKEN,
        "accept": "application/json"
    }

    # 3. Отправляем запрос
    response = requests.get(url, headers=headers)

    # 4. Проверяем, что статус-код 200
    assert response.status_code == 200, f"Ожидали 200, но получили {response.status_code}"

    # 5. Проверяем, что в ответе есть фильм, выбранный случайным образом
    data = response.json()
    assert "id" in data, "В ответе отсутствует поле 'id'"

    print("Тест пройден! Найден случайный фильм.")


# --- ТЕСТ 5: ПОЛУЧЕНИЕ ФИЛЬМА ПО НЕВАЛИДНОМУ ID ---
@pytest.mark.api
def test_search_movie_by_invalid_id():
    # 1. Формируем адрес запроса
    url = f"{settings.BASE_URL}/v1.5/movie/999999999999999"

    # 2. Формируем заголовки
    headers = {
        "X-API-KEY": settings.API_TOKEN,
        "accept": "application/json"
    }

    # 3. Отправляем запрос
    response = requests.get(url, headers=headers)

    # 4. Проверяем, что статус-код 400
    assert response.status_code == 400, f"Ожидали 400, но получили {response.status_code}"

    # 5. Проверяем, что в ответе есть ошибка
    data = response.json()
    assert "error" in data, "В ответе нет поля 'error'"

    print("Тест пройден! Фильм по невалидному id не найден.")


# --- ТЕСТ 6: ПОИСК ФИЛЬМА БЕЗ ТОКЕНА АВТОРИЗАЦИИ ---
@pytest.mark.api
def test_search_movie_without_token():
    # 1. Формируем адрес запроса
    url = f"{settings.BASE_URL}/v1.5/movie/search"

    # 2. Формируем заголовки
    headers = {
        "accept": "application/json"
    }

    # 3. Формируем параметры (что ищем)
    params = {
        "query": "Начало"
    }

    # 4. Отправляем запрос
    response = requests.get(url, headers=headers, params=params)

    # 5. Проверяем, что статус-код 401
    assert response.status_code == 401, f"Ожидали 401, но получили {response.status_code}"

    # 6. Проверяем, что в ответе ошибка
    data = response.json()
    assert "error" in data, "В ответе нет поля 'error'"

    print("Тест пройден! Фильм без токена авторизации невозможно найти.")
