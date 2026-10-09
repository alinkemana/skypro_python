import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Принимает на вход текст, делает первую букву заглавной
# и возвращает этот же текст


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("skyPro", "SkyPro"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Принимает на вход текст и удаляет пробелы в начале, если они есть


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("    Skypro", "Skypro"),
    ("    123 hello world", "123 hello world"),
    ("    123456", "123456"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("     ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Возвращает `True`, если строка содержит искомый символ
# и `False` - если нет


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "k", True),
    ("hello world", "h", True)
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "h", False),
    ("", "k", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# Удаляет все подстроки из переданной строки


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "k", "sypro"),
    ("hello world", "l", "heo word")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "h", "skypro"),
    ("", "k", ""),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
