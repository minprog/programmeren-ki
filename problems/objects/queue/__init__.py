import check50
import uva.check50.py
import check50.internal
import sys
import os
import inspect
import string
import random

check50.internal.register.before_every(lambda : sys.path.append(os.getcwd()))
check50.internal.register.after_every(lambda : sys.path.pop())

error_text = "the queue.py program did not work correctly"
help_text = "sorry, no hints on this one. please test your class using the instructions in the lab"


@check50.check()
def exists():
    """queue.py exists."""
    check50.exists("queue.py")


@check50.check(exists)
def works():
    """queue.py works correctly."""
    try:
        uva.check50.py.compile("queue.py")
        module = uva.check50.py.run("queue.py").module

        # check if the class exists
        if not hasattr(module, "Queue"):
            raise Exception()
        
        # check if all required methods exist
        for method in ['enqueue', 'dequeue', 'peek', 'size', 'empty']:
            if not hasattr(module.Queue, method) or not callable(getattr(module.Queue, method)):
                raise Exception()
        
        # generate a list to run tests on
        tests = list(string.ascii_uppercase)
        tests += list(range(10))
        random.shuffle(tests)

        # create an instance of Queue
        queue = module.Queue()

        # enqueue everything
        for test in tests:
            queue.enqueue(test)

        # dequeue and compare half of the entries
        for i, test in enumerate(tests):
            if i > len(tests) / 2:
                break

            assert test == queue.peek()
            assert queue.size() == len(tests) - i
            assert test == queue.dequeue()

        # clear queue and add one item
        test = random.choice(tests)
        queue.empty()
        queue.enqueue(test)

        # test if clear was succesful
        assert test == queue.peek()
        assert queue.size() == 1
        assert test == queue.dequeue()
        assert queue.size() == 0

        # test if dequeueing on an empty queue throws an AssertionError
        try:
            queue.dequeue()
            raise Exception()
        except AssertionError as e:
            pass
        
    except Exception as e:
        # throw a general error if anything fails
        raise check50.Failure(error_text, help=help_text)
