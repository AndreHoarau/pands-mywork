# This program will take in numbers and return a list conatining a 
# Fibonaccis sequence of that many numbers.
# Author Andre Hoarau
import logging
#logging.basicConfig(level=logging.debug)
def fibonacci(number):
    if number == 0:
        return []
    if number < 0:
        raise ValueError('number must be >0')
    a = 0 
    b = 1
    fiboncaciSequence= [0]
    # we have one in the list already so number - 1 times
    # this is not the most efficient code
    # could have used yield
    for i in range(1,number):
        fiboncaciSequence.append(b)
        # this is a funky code make a = ba and b = a + b
        a, b = b, a + b 
    #logging.debug("%d: %s", number, fiboncaciSequence).
    return fiboncaciSequence


if __name__== '__main__':
# tests will go here
    return7 = [0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    assert fibonacci(7) == return7, ' incorrect return for 7'
    assert fibonacci(11) == return11, 'incorrect return for 11'
    assert fibonacci(0) == [], 'incorrect return value for 0'
    assert fibonacci(1) == [0], 'incorrect return value for 1'
    try: 
        fibonacci(-1)
    except ValueError:
        # we want this exception to be thrown
        # so this is an exapmle where we want to do nothing
        pass
    else:
        # if the exception was not thrown we should throw
        # Assertion error
        assert False, 'fibonacci missing ValueError'
        # or
        # raise AssertionError("fibonacci no valueError")
    print('all good')

