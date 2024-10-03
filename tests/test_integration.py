from lib.diary import Diary 
from lib.diary_entry import DiaryEntry


def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "My contents")
    entry_2 = DiaryEntry("Breakfast", "I had cereal")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

def test_count_words_multiple_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "My contents")
    entry_2 = DiaryEntry("Breakfast", "I had cereal")
    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.count_words() == 5

def test_reading_time_multiple_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "My contents")
    entry_2 = DiaryEntry("Breakfast", "I had cereal")
    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.reading_time(10) == 0.5

def test_find_best_entry_for_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of this entry")
    entry_2 = DiaryEntry("Breakfast", "A quick brown fox jumps over the bing bong waloop hello world")
    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.find_best_entry_for_reading_time(2, 5) == entry_2
