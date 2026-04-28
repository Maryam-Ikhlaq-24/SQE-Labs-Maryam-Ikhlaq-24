# week1/test_string_utils.py

import pytest
from string_utils import *


# ---------------- count_vowels ----------------
def test_count_vowels_normal():
    assert count_vowels("Hello") == 2

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_case_insensitive():
    assert count_vowels("AEIOU") == 5


# ---------------- reverse_string ----------------
def test_reverse_string_basic():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single_char():
    assert reverse_string("a") == "a"

def test_reverse_string_spaces():
    assert reverse_string("  hi") == "ih  "


# ---------------- is_palindrome ----------------
def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True

def test_is_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False


# ---------------- word_count ----------------
def test_word_count_normal():
    assert word_count("Hello World") == 2

def test_word_count_spaces():
    assert word_count("   spaces   ") == 1

def test_word_count_empty():
    assert word_count("") == 0


# ---------------- capitalise_words ----------------
def test_capitalise_words_basic():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_words_mixed_case():
    assert capitalise_words("hELLo WoRLD") == "Hello World"

def test_capitalise_words_single():
    assert capitalise_words("python") == "Python"


# ---------------- remove_duplicates ----------------
def test_remove_duplicates_basic():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_remove_duplicates_long_sequence():
    assert remove_duplicates("aaaaa") == "a"

def test_remove_duplicates_mixed():
    assert remove_duplicates("aabbccdde") == "abcde"


# ---------------- exception test ----------------
def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        count_vowels(None)