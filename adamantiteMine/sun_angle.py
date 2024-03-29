#!/usr/bin/env checkio --domain=epy run sun-angle
def sun_angle(time):
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])
    if hour < 6 or hour > 18 or hour == 18 and minute > 0:
        return "I don't see the sun!"
    else:
        return (hour - 6) * 15 + minute * 15 / 60


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
