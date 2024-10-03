from lib.diary import Diary


def test_diary_initially_empty():
    diary = Diary()
    assert diary.all() == []

def test_diary_word_count_initially_is_zero():
    diary = Diary()
    assert diary.count_words() == 0
