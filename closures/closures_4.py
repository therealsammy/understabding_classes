import logging
"""
Import the logging module to show the function logs
Save the logs to a file named 'example.log'
"""
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(subtract)

add_logger(3, 3)
sub_logger(10, 5)


