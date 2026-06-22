import pytest
from string_utils import StringUtils


string_utils = StringUtils()
# 1


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   ")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# 2
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" honor", "honor"),
    ("  parade", "parade"),
    ("   victory", "victory"),
    ("    Spider-man", "Spider-man")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Tony", "Tony"),
    ("  ", " "),
    ("BrianMaps", "BrianMaps"),
    ("", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# 3
@pytest.mark.positive
@pytest.mark.parametrize("str1, str2, result", [
    ("Eleven", "El", True),
    ("Eleven", "n", True),
    ("Eleven", "o", False),
    ("Eleven", "e", True),
    ("Eleven", "p", False)
])
def test_contains_positive(str1, str2, result):
    assert string_utils.contains(str1, str2) == result


@pytest.mark.negative
@pytest.mark.parametrize("str1, str2, result", [
    ("Cyberpunk", "peak", True),
    ("Anastasos", "n", True),
    ("Red Dead", "o", False),
    (" ", "  -", True),
    ("Marvel", "", True)
])
def test_contains_negative(str1, str2, result):
    assert string_utils.contains(str1, str2) == result


# 4
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Angela", "a", "Angel"),
    ("12345", "45", "123"),
    ("The_100", "The", "_100")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "", ""),
    ("12345", "45", "123"),
    ("   ", "   ", ""),
    ("The_100", "The", "_100")
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
