'''
Decorator for retrying a function N times when one of the specified exceptions is raised.

Author: fjsj - flaviojuvenal@gmail.com
'''
import os

def retry_on_exceptions(types, tries):
    class RetryException(Exception): #Exception to activate retries
        pass
    
    def call_and_ignore_exceptions(types, fxn, *args, **kwargs):
        try:
            return fxn(*args, **kwargs)
        except Exception, exc:
            if any((isinstance(exc, exc_type) for exc_type in types)):
                raise RetryException()
            else:
                raise exc #raise up unknown error
    
    def decorator(fxn):
        def f_retry(*args, **kwargs):
            local_tries = tries #make mutable
            while local_tries > 1:
                try:
                    return call_and_ignore_exceptions(types, fxn, *args, **kwargs)
                except RetryException:
                    local_tries -= 1
                    print "Retrying function %s" % fxn.__name__
            
            print "Last try... and I will raise up whatever exception is raised"
            return fxn(*args, **kwargs)
        return f_retry
    return decorator

