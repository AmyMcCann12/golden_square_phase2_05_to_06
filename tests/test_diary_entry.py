import pytest #type: ignore
from lib.diary_entry import *

# Test the format method of diary_entry

def test_diary_entry_format_empty_contents():
    diary_entry = DiaryEntry("My Diary", "")
    with pytest.raises(Exception) as e:
        diary_entry.format()
    assert str(e.value) == "Diary Contents is Empty"

def test_diary_entry_format_contents():
    diary_entry = DiaryEntry("My Diary", "These are the contents of my diary")
    assert diary_entry.format() == "My Diary: These are the contents of my diary"

# Test the count_words method of diary_entry

def test_count_words_contents_is_sentence():
    diary_entry = DiaryEntry("My Diary", "Hello and welcome to my diary.")
    assert diary_entry.count_words() == 6

def test_count_words_contents_is_empty():
    diary_entry = DiaryEntry("My Diary", "")
    assert diary_entry.count_words() == 0

# Test the reading_time method of diary_entry

def test_reading_time_contents_is_empty():
    diary_entry = DiaryEntry("My Diary", "")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(200)
    assert str(e.value) == "Diary contents is empty, no reading time can be calculated."

def test_reading_time_contents_has_200_words():
    text = " ".join(["word" for i in range(0, 200)])
    diary_entry = DiaryEntry("My Diary", text)
    assert diary_entry.reading_time(200) == 1

def test_reading_time_contents_has_400_words():
    text = " ".join(["word" for i in range(0, 400)])
    diary_entry = DiaryEntry("My Diary", text)
    assert diary_entry.reading_time(200) == 2

def test_reading_time_contents_has_100_words():
    text = " ".join(["word" for i in range(0, 100)])
    diary_entry = DiaryEntry("My Diary", text)
    assert diary_entry.reading_time(200) == 1

def test_reading_time_wpm_zero():
    diary_entry = DiaryEntry("My Diary", "one two three four")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "wpm cannot be zero, no reading time can be calculated"

# Test reading chunk for empty contents

# Test reading_chunk for one call
def test_reading_chunk_one_call():
    text = "one two three four five six seven eight nine ten"
    diary_entry = DiaryEntry("My Diary", text )
    assert diary_entry.reading_chunk(5,1) == "one two three four five"

# Test reading chunk for 2 calls
def test_reading_chunk_two_calls():
    text = "one two three four five six seven eight nine ten"
    diary_entry = DiaryEntry("My Diary", text)
    assert diary_entry.reading_chunk(5,1) == "one two three four five"
    assert diary_entry.reading_chunk(5,1) == "six seven eight nine ten"

# Test reading chunk for multiple calls

def test_reading_chunk_four_calls():
    text = """one two three four five six seven eight nine ten 
    one two three four five six seven eight nine ten 
    one two three four five six seven eight nine ten"""
    diary_entry = DiaryEntry("My Diary", text)
    assert diary_entry.reading_chunk(4,1) == "one two three four"
    assert diary_entry.reading_chunk(2,1) == "five six"
    assert diary_entry.reading_chunk(3,2) == "seven eight nine ten one two"
    assert diary_entry.reading_chunk(5,1) == "three four five six seven"

# Test reading chunk to end of text then wrap round again.
def test_reading_chunk_restart_once_all_text_read():
    text = "one two three four five six seven eight nine ten"
    diary_entry = DiaryEntry("My Diary", text)
    assert diary_entry.reading_chunk(2,2) == "one two three four"
    assert diary_entry.reading_chunk(7,1) == "five six seven eight nine ten"
    assert diary_entry.reading_chunk(3,1) == "one two three"
