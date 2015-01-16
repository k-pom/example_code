#!/usr/bin/env python


def to_long(string, base=10):
    """
        Given a well formatted string and an optional base, convert the string
        into a long.

        This supports only well formed strings, including hex notation, long
        notation and negatives.

        This does not support anything with decimals, commas, or other special
        characters.
    """

    if type(base) != int:
        raise TypeError("Unsupported type %s" % type(base))

    if base < 2 or base > 16:
        raise TypeError("Unsupported base %s" % base)

    # If it is anything other than a string, bail. Alternatively, we could
    # explicity cast it to a str if we wanted to try anyways.
    if type(string) != str:
        raise TypeError("Unsupported type %s" % type(string))

    # If it is negative, pop the '-' off and store that data for later
    negative = False
    if string[0] == "-":
        string = string[1:]
        negative = True

    # Long notation in python is to append an 'L'. Remove it if present
    if string[-1].upper() == "L":
        string = string[:-1]

    # Hex notation, remove the 0x
    if base == 16 and string[0:2] == "0x":
        string = string[2:]

    # Starting at the ones place, with a total value of 0
    current_place_value = 1
    current_value = 0L

    # Iterating over the string, starting with the lowest value
    for c in reversed(string):

        # Get the value of the character from the dict below
        char_value = character_values.get(c.lower(), None)

        # If the value is not in our list or it doesn't make sense for the base
        if char_value is None or char_value >= base:
            raise ValueError("Invalid character %s for base %s" % (c, base))

        # Multiple the value of the character times the place value
        current_value += (char_value * current_place_value)

        # Add the real value of the character to the total
        current_place_value = current_place_value * base

    # Use the negative value we saved earlier
    if negative:
        current_value = current_value * -1

    return current_value


character_values = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}
