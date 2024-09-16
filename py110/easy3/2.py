MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def before_midnight(date):
    hour = int(date.split(":")[0])
    minutes = int(date.split(":")[1])
    return (MINUTES_PER_DAY - (hour * MINUTES_PER_HOUR + minutes)) % MINUTES_PER_DAY

def after_midnight(date):
    hour = int(date.split(":")[0])
    minutes = int(date.split(":")[1])
    return (hour * MINUTES_PER_HOUR + minutes) % MINUTES_PER_DAY

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True