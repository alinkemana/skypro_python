from db import SubjectTable

CONNECTION_STRING = "postgresql://postgres:26105@localhost:5432/postgres"
db = SubjectTable(CONNECTION_STRING)


def test_create_subject():
    title = "Test Subject"
    db.create(title)
    max_id = db.get_max_id()

    rows = db.get_by_id(max_id)
    assert len(rows) == 1
    assert rows[0][1] == title  # [1] — это вторая колонка (subject_title)

    db.delete(max_id)


def test_edit_subject():
    title = "Old Subject"
    db.create(title)
    max_id = db.get_max_id()

    new_title = "New Subject"
    db.update_title(max_id, new_title)

    rows = db.get_by_id(max_id)
    assert len(rows) == 1
    assert rows[0][1] == new_title

    db.delete(max_id)


def test_delete_subject():
    title = "To Be Deleted"
    db.create(title)
    max_id = db.get_max_id()

    db.delete(max_id)

    rows = db.get_by_id(max_id)
    assert len(rows) == 0
