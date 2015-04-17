from retry import retry_on_exceptions
import logging
from unittest import TestCase, main

# set root logger to console
l = logging.getLogger()
l.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fm = logging.Formatter('[%(levelname)s] %(asctime)s %(threadName)-10s - %(message)s')
ch.setFormatter(fm)
l.addHandler(ch)


class RetryTest(TestCase):

    def setUp(self):
        self.current_try = 0

    def test_retry(self):
        @retry_on_exceptions(types=[ZeroDivisionError, KeyError], tries=3)
        def f():
            self.current_try += 1
            if self.current_try == 1:
                return 1 / 0
            elif self.current_try == 2:
                return dict()['key']
            else:
                return "Got it on last try!"
        self.assertEquals(f(), "Got it on last try!")
        self.assertEquals(self.current_try, 3)

    def test_execute_functions_on_retry_fail_n_times(self):
        self.current_try = 0
        self.executed = False

        def function_to_be_executed():
            logging.debug("Executing function")
            self.executed = True

        @retry_on_exceptions(types=[ZeroDivisionError], tries=3, func=function_to_be_executed)
        def fail():
            self.current_try += 1
            if self.current_try < 4:
                return 1 / 0
            else:
                return "It will never get here!"
        try:
            fail()
        except ZeroDivisionError:
            self.assertEquals(self.executed, True)
            self.assertEquals(self.current_try, 3)


if __name__ == "__main__":
    main()
