import math

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.start_reading = 0

    def format(self):
        if self.contents == "":
            raise Exception("Diary Contents is Empty")
        formatted_diary = f"{self.title}: {self.contents}"
        return formatted_diary

    def count_words(self):
        words_list = self.contents_words()
        counter = len(words_list)
        return counter

    def reading_time(self, wpm):
        if self.contents == "":
            raise Exception("Diary contents is empty, no reading time can be calculated.")
        if wpm == 0:
            raise Exception("wpm cannot be zero, no reading time can be calculated")
        reading_time_count = math.ceil(len(self.contents_words()) / wpm)
        return reading_time_count
    
    def reading_chunk(self, wpm, minutes):
        number_words_to_read = wpm * minutes
        reading_chunk = self.contents_words()[self.start_reading:(self.start_reading + number_words_to_read)]
        if self.start_reading + number_words_to_read >= len(self.contents_words()):
            self.start_reading = 0
        else:
            self.start_reading += number_words_to_read
        return " ".join(reading_chunk[:number_words_to_read])

    def contents_words(self):
        return self.contents.split()