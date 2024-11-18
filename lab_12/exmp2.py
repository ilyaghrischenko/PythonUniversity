class WeekDayError(Exception):
    pass


class Weeker:
    DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in self.DAYS:
            raise WeekDayError
        self._day = day

    def __str__(self):
        return self._day

    def add_days(self, n):
        current_index = self.DAYS.index(self._day)
        new_index = (current_index + n) % 7
        self._day = self.DAYS[new_index]

    def subtract_days(self, n):
        current_index = self.DAYS.index(self._day)
        new_index = (current_index - n) % 7
        self._day = self.DAYS[new_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
