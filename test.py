import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("аеёиоуыэюяАЕЁИОУЫЭЮЯ") == 20

def test_no_vowels():
    assert count_vowels("бвгджзйклмнпрстфхцчшщ") == 0

def test_mixed_string():
    assert count_vowels("Привет Мир") == 3
    assert count_vowels("Тестирование") == 7
    assert count_vowels("ПРОГРАММИРОВАНИЕ") == 7
    assert count_vowels("12345!@#") == 0
