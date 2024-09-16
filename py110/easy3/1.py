def time_of_day(number):
    # DO NOT HARD CODE FUCKING CONSTANTS
    hours = str((number // 60) % 24).rjust(2, '0')
    minutes = str(number % 60).rjust(2, '0')
    return f"{hours}:{minutes}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True