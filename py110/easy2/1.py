# Algorithm

# Take the floating point number as input
# Convert it to a string to extract the degree
# Extract the decimal part from the string too
# Convert it back to a float
# Convert the last result to a string, extract the integer part and use
#   it as the minutes, then get the seconds the same way

def dms(angle):
    DEGREE = "\u00B0"
    int_part, dec_part = int(angle), angle - int(angle)

    # minutes
    minutes_decimal = dec_part * 60
    minutes, seconds_part = int(minutes_decimal), minutes_decimal - int(minutes_decimal)
    display_minutes = str(minutes).rjust(2, '0')

    # seconds
    seconds = int(seconds_part * 60)
    display_seconds = str(seconds).rjust(2, '0')
    return(f"{int_part}{DEGREE}{display_minutes}'{display_seconds}\"")


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")