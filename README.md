# retry\_on\_exceptions decorator
Decorator for retrying a function N times when one of the specified exceptions is raised.
Specially useful for functions that throws errors sporadically, like ones that depends on external resources as web APIs, databases, etc.

Usage:

    from retry import retry_on_exceptions

    current_try = 0
    @retry_on_exceptions(types=[ZeroDivisionError, KeyError], tries=3)
    def test():
        global current_try
        current_try += 1
        if current_try == 1:
            return 1 / 0
        elif current_try == 2:
            return dict()['key']
        else:
            return "Got it on last try!"    

    if __name__ == "__main__":
        print test()

The code above prints:

- Retrying function test
- Retrying function test
- Last try... and I will raise up whatever exception is raised
- Got it on last try!

