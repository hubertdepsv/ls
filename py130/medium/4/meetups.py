# a year and a month create the object
# a day method gets a day of week and a descriptor as input (case insensitive)
# it returns a datetime object
# e.g.: (2nd tuesday), with month and year set -> dd.mm.yyyy of the meetup

# algorithm
# create a datetime object with the first day of the month
# 1 DOWM = 1 - 7
# 2 DOWM = 8 - 14
# 3 DOWM = 15 - 21
# 4 DOWM = 22 - 28
# 5 DOWM = 29 - 31

# April, June, September, and November have 30 days.
# February has 28 in most years, but 29 in leap years. (year // 4 == 0)
# All the other months have 31 days.

from datetime import date, timedelta

class Meetup:
    DESCRIPTOR_MAP = {
        'first': 0,
        'second': 1,
        'third': 2,
        'fourth': 3,
        'fifth': 4,
        'last': -1,
        'teenth': [12, 19]
    }

    WEEKDAY_MAP = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6,
    }

    def __init__(self, year, month):
        self.month = month
        self.year = year

    def day(self, day, descriptor):
        day = Meetup.WEEKDAY_MAP[day.casefold()]
        descriptor = descriptor.casefold()
        descriptor = Meetup.DESCRIPTOR_MAP[descriptor] if descriptor != 'teenth' else descriptor

        # first and last days of the month
        if self.month < 12:
            last_day_of_month = date(self.year, self.month + 1, 1) - timedelta(days=1)
        else:
            last_day_of_month = date(self.year + 1, self.month, 1) - timedelta(days=1)

        number_of_days = last_day_of_month.day

        # if I have the 2nd tuesday, then
        # find the monthly index of all tuesdays
        possible_days = [date(self.year, self.month, day_index) for day_index in range(1, number_of_days + 1)
                         if date(self.year, self.month, day_index).weekday() == day]
        
        if descriptor == 'teenth':
            return [day for day in possible_days if (12 < day.day < 20)][0]
        
        if descriptor > len(possible_days) - 1:
            return None

        return possible_days[descriptor]