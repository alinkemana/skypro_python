# Дипломный проект: Автотесты для Кинопоиска

## Описание
Проект содержит автотесты для тестирования веб-интерфейса (UI) сайта kinopoisk.ru и его REST API (api.kinopoisk.dev). 
Включает в себя API-тесты (проверка поиска, фильтрации, получения данных) и UI-тесты (поиск фильмов, чтение карточки фильма, чтение данных об актерах, фильтрация фильмов).

## Стек технологий
- Python 3
- Pytest
- Requests (для API)
- Selenium (для UI)
- Allure (для отчетов)
- Flake8 (для стиля кода)

## Установка и запуск
1. Клонируйте репозиторий.
2. Создайте виртуальное окружение: `python3 -m venv .venv`
3. Активируйте его: `source .venv/bin/activate`
4. Установите зависимости: `pip install -r requirements.txt`
5. Создайте файл `.env` на основе `.env.example` и вставьте туда ваш API_TOKEN.

## Режимы запуска тестов
- Запустить все тесты: `pytest`
- Запустить только API-тесты: `pytest -m "api"`
- Запустить только UI-тесты: `pytest -m "ui"`
- Запустить с генерацией Allure-отчета: `pytest --alluredir=allure-results`

## Ссылки
- Страница проекта в Yonote: (https://alink.yonote.ru/doc/testirovanie-funkcionala-kinopoiska-V8G3r0IFJX#h-vidy-testirovaniya-i-okruzhenie)
