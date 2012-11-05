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

if __name__ == "__main__":
    main()
