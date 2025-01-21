class Clock:
    ONE_HOUR = 60
    ONE_DAY = 24 * ONE_HOUR
    
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes if minutes else 0
        self.total_minutes = self.minutes + self.hours * Clock.ONE_HOUR

    @classmethod
    def at(cls, hours, minutes=None):
        return Clock(hours, minutes)

    def __add__(self, other):
        hours, minutes = self._get_new_total(other + self.total_minutes)
        return Clock.at(hours, minutes)

    def __sub__(self, other):
        hours, minutes = self._get_new_total(self.total_minutes - other)
        return Clock.at(hours, minutes)

    def __str__(self):
        padded_minutes = self.minutes if self.minutes > 9 else '0' + str(self.minutes)
        padded_hours = self.hours if self.hours > 9 else '0' + str(self.hours)
        return f"{padded_hours}:{padded_minutes}"
    
    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes
    
    @staticmethod
    def _get_new_total(total_minutes):
        _, hours = divmod(total_minutes, Clock.ONE_DAY)
        return divmod(hours, Clock.ONE_HOUR)