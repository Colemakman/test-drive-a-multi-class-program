from lib.diary_entry import DiaryEntry


def test_formatting_entry():
    entry = DiaryEntry("Hello", "This is my entry")
    assert entry.format() == "Hello: This is my entry"

def test_count_words():
    entry = DiaryEntry("Hello", "This is my entry")
    assert entry.count_words() == 4

def test_reading_time():
    entry = DiaryEntry("Hello", "This is my entry")
    assert entry.reading_time(1) == 4 and entry.reading_time(2) == 2

def test_reading_chunk():
    entry = DiaryEntry("My Entry", "One two three four five six seven eight nine ten")
    assert entry.reading_chunk(2, 3) == "One two three four five six"
