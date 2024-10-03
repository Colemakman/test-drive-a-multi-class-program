# File: lib/diary.py

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list

        self.entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry

        return self.entries
        
    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.

        total = 0
        for entry in self.all():
            total += entry.count_words()

        return total

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.

        total = 0
        for entry in self.all():
            total += entry.reading_time(wpm)

        return total

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.

        best_entry = None
        best_diff = float('inf')
        for entry in self.all():
            time = entry.reading_time(wpm)
            if time <= minutes and minutes - time < best_diff:
                best_diff = minutes - time
                best_entry = entry

        return entry

