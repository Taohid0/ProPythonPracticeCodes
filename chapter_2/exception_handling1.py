import logging

def count_lines(filename):
    try:
        file = open(filename, "r")
    except TypeError as e:
        logging.error(e)
        return 0
    except EnvironmentError as e:
        logging.error(e.args[1])
        return 0
    else:
        return len(file.readlines())