'''
Decorator for retrying a function N times by catching one of the specified exceptions and then retrying

Author: fjsj - flaviojuvenal@gmail.com
'''
import logging
import time


def retry_on_exceptions(types, tries, delay=0, func=None):
    class RetryException(Exception):  # Exception to activate retries
        pass

    def call_and_ignore_exceptions(types, fxn, *args, **kwargs):
        try:
            return fxn(*args, **kwargs)
        except Exception, exc:
            if any((isinstance(exc, exc_type) for exc_type in types)):
                raise RetryException()
            else:
                raise exc  # raise up unknown error

    def decorator(fxn):
        def f_retry(*args, **kwargs):
            local_tries = tries  # make mutable
            while local_tries > 1:
                try:
                    return call_and_ignore_exceptions(types, fxn, *args, **kwargs)
                except RetryException:
                    local_tries -= 1
                    if delay:
                        logging.debug("Waiting %s seconds to retry %s..." % (delay, fxn.__name__))
                        time.sleep(delay)  # sleep only current thread
                    logging.debug("Retrying function %s" % fxn.__name__)
            else:
                if func is not None:
                    return func()

            logging.debug("Last try... and I will raise up whatever exception is raised")
            return fxn(*args, **kwargs)
        return f_retry
    return decorator
