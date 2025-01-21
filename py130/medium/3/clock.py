class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes if minutes else 0

    @classmethod
    def at(cls, hours, minutes=None):
        return Clock(hours, minutes)

    def __add__(self, other):
        total_minutes = other + self.hours * 60 + self.minutes
        _, other = divmod(total_minutes, 1440)
        hours, minutes = divmod(other, 60)
        return Clock.at(hours, minutes)

    def __sub__(self, other):
        total_minutes = self.hours * 60 + self.minutes - other
        _, other = divmod(total_minutes, 1440)
        hours, minutes = divmod(other, 60)
        return Clock.at(hours, minutes)

    def __str__(self):
        padded_minutes = self.minutes if self.minutes > 9 else '0' + str(self.minutes)
        padded_hours = self.hours if self.hours > 9 else '0' + str(self.hours)
        return f"{padded_hours}:{padded_minutes}"
    
    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes