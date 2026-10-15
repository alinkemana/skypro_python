import os
import requests
from config import BASE_URL
from config import TIMEOUT


class ProjectPage:
    def __init__(self):
        self.base_url = f"{BASE_URL}/projects"

        # Берём токен из переменной окружения.
        self.token = os.getenv("YOUGILE_TOKEN")
        if not self.token:
            raise ValueError("Не задана переменная окружения YOUGILE_TOKEN")

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    # создать проект. POST /api-v2/projects
    def create_project(self, new_project):
        response = requests.post(
            self.base_url,
            json=new_project,
            headers=self.headers,
            timeout=TIMEOUT
        )
        return response

    # изменить проект. PUT /api-v2/projects/{id}
    def update_project(self, project_id, new_project):
        url = f"{self.base_url}/{project_id}"
        response = requests.put(
            url,
            json=new_project,
            headers=self.headers,
            timeout=TIMEOUT
        )
        return response

    # получить проект по ID. GET /api-v2/projects/{id}
    def get_project(self, project_id):
        url = f"{self.base_url}/{project_id}"
        response = requests.get(
            url,
            headers=self.headers,
            timeout=TIMEOUT
        )
        return response

    # очистить
    def delete_project(self, project_id):
        url = f"{self.base_url}/{project_id}"
        return requests.put(
            url,
            json={"deleted": True},
            headers=self.headers,
        )
