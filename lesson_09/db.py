from sqlalchemy import create_engine
from sqlalchemy.sql import text


class SubjectTable:
    __scripts = {
        "insert_new": text(
            "INSERT INTO subject (subject_title) VALUES (:new_title)"
        ),
        "get_max_id": text("SELECT MAX(subject_id) FROM subject"),
        "select_by_id": text(
            "SELECT * FROM subject WHERE subject_id = :select_id"
        ),
        "update_title": text(
            "UPDATE subject SET subject_title = :new_title "
            "WHERE subject_id = :subject_id"
        ),
        "delete_by_id": text(
            "DELETE FROM subject WHERE subject_id = :id_to_delete"
        ),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create(self, title):
        self.__db.execute(
            self.__scripts["insert_new"],
            new_title=title
        )

    def get_max_id(self):
        return self.__db.execute(
            self.__scripts["get_max_id"]
        ).fetchall()[0][0]

    def get_by_id(self, id):
        return self.__db.execute(
            self.__scripts["select_by_id"],
            select_id=id
        ).fetchall()

    def update_title(self, id, new_title):
        self.__db.execute(
            self.__scripts["update_title"],
            new_title=new_title,
            subject_id=id
        )

    def delete(self, id):
        self.__db.execute(
            self.__scripts["delete_by_id"],
            id_to_delete=id
        )
