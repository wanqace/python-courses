#!/usr/bin/env python
import logging
logging.basicConfig(level=logging.DEBUG)


def is_balanced_2(string, br):
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


def is_balanced(string, br):
    br_open, br_close = br[::2], br[1::2]
    br_only = filter(lambda s: s in br, list(string))
    stack = []
    for s in br_only:
        # Pure open
        if s in br_open and s not in br_close:
            logging.debug('Pure open {0}'.format(s))
            stack.append(s)
        # Pure close
        elif s in br_close and s not in br_open:
            if stack and br_open.index(stack[-1]) == br_close.index(s):
                logging.debug('Pure close {0}'.format(s))
                stack.pop()
            else:
                return False
        # Quotes (open == close)
        elif stack and stack[-1] == s:
            logging.debug('Quote close {0}'.format(s))
            stack.pop()
        else:
            logging.debug('Quote open {0}'.format(s))
            stack.append(s)
    logging.debug('Result stack: {0}'.format(stack))
    return not stack


print is_balanced("(Sensei says yes!)", "()")       # => True
print is_balanced("(Sensei says no!", "()")         # => False
print is_balanced("(Sensei [says] yes!)", "()[]")   # => True
print is_balanced("(Sensei [says) no!]", "()[]")    # => False
print is_balanced("Sensei says 'yes'!", "''")       # => True
print is_balanced("Sensei say's no!", "''")         # => False
