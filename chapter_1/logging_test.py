import logging

try:
    print(1 / 0)
except ZeroDivisionError as ex:
    logging.error(ex)
