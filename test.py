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
