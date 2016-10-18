#!/usr/bin/env python


def is_balanced(string, br):
    # filter only brackets
    br_only = filter(lambda s: s in br, list(string))
    # Must be even
    if len(br_only) % 2:
        return False
    # Opening brackets list
    br_open = br[::2]
    # Closing brackets list
    br_close = br[1::2]
    while br_only:
        # Popped first and last brackets must be corresponding
        if br_open.index(br_only.pop(0)) != br_close.index(br_only.pop()):
            return False
    # Empty list, all criteria are met
    return True


print is_balanced("(Sensei says yes!)", "()")       # => True
print is_balanced("(Sensei says no!", "()")         # => False
print is_balanced("(Sensei [says] yes!)", "()[]")   # => True
print is_balanced("(Sensei [says) no!]", "()[]")    # => False
print is_balanced("Sensei says 'yes'!", "''")       # => True
print is_balanced("Sensei say's no!", "''")         # => False
