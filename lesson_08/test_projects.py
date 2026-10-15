import pytest

from project_page import ProjectPage


@pytest.fixture
def project_page():
    return ProjectPage()


# тесты для метода POST - создание проекта
# Позитивный тест: создаём проект с валидными данными.
def test_create_project_positive(project_page):
    new_project = {"title": "Мой тестовый проект"}
    response = project_page.create_project(new_project)

    assert response.status_code == 201

    # Проверяем, что в ответе есть ID созданного проекта
    response_data = response.json()
    assert response_data.get("id"), f"Пустой id: {response_data}"

    # Чистим за собой
    project_page.delete_project(response_data["id"])


# Негативный тест: создаем проект без обязательного поля
# Поле "title" отсутствует.
def test_create_project_negative(project_page):

    response = project_page.create_project({})

    # Ожидаем ошибку 400 или 422
    assert response.status_code in [400, 422]

    # Проверяем, что в ответе есть сообщение об ошибке
    body = response.json()
    error_text = body.get("error") or body.get("message")
    assert error_text, f"Нет сообщения об ошибке: {body}"


# тесты для метода PUT - изменение проекта
# Позитивный тест: создаём проект, потом меняем его название.
def test_update_project_positive(project_page):
    created = project_page.create_project(
        {"title": "Старое название"}
    )
    project_id = created.json()["id"]

    # Меняем название
    try:
        new_title = "Новое название"
        response = project_page.update_project(
            project_id, {"title": new_title}
        )
        assert response.status_code == 200

        # Запрашиваем проект и проверяем название
        get_response = project_page.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json()["title"] == new_title
    finally:
        project_page.delete_project(project_id)


# Негативный тест: изменяем название проекта с несуществующим ID.
def test_update_project_negative(project_page):
    fake_id = "00000000-0000-0000-0000-000000000000"

    response = project_page.update_project(fake_id, {"title": "фейк"})

    # Проекта с таким ID нет — ожидаем ошибку
    assert response.status_code in [400, 403, 404]

    # Проверяем, что есть описание ошибки
    body = response.json()
    error_text = body.get("error") or body.get("message")
    assert error_text, f"API не вернул сообщение об ошибке: {body}"


# тесты для метода GET - получение проекта
# Позитивный тест: создаём проект, потом запрашиваем его по ID.
def test_get_project_positive(project_page):
    created = project_page.create_project({"title": "Проект GET"})
    project_id = created.json()["id"]

    # Запрашиваем созданный проект
    try:
        response = project_page.get_project(project_id)

        # Ожидаем 200
        assert response.status_code == 200

        # Проверяем, что в ответе тот же ID
        assert response.json()["id"] == project_id
    finally:
        project_page.delete_project(project_id)


# Негативный тест: запрашиваем проект с несуществующим ID.
def test_get_project_negative(project_page):
    fake_id = "00000000-0000-0000-0000-000000000000"

    response = project_page.get_project(fake_id)

    # Ожидаем ошибку
    assert response.status_code in [400, 403, 404]

    # Проверяем, что есть описание ошибки
    body = response.json()
    error_text = body.get("error") or body.get("message")
    assert error_text, f"Нет сообщения об ошибке: {body}"
