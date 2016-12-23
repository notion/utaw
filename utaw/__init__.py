"""
UTAW - Unit Test Assertion Wrapper.

Wraps the python builtin unittest assertions in a library that doesn't require you to instantiate a TestCase.
"""


# [ Imports ]
import unittest
import sys


# [ Globals ]
# get self to remove spurious attributes
self = sys.modules[__name__]
# use a real test case because the assertion reporting uses instance methods.
TESTCASE = unittest.TestCase()
# always report the full diff
TESTCASE.maxDiff = None
# vulture
assert not TESTCASE.maxDiff


# [ Add TestCase Assertions ]
for attribute in dir(TESTCASE):
    # only provide access to the assertions
    if attribute.startswith('assert'):
        self.__dict__[attribute] = getattr(TESTCASE, attribute)


# [ Clean Up Intermediate Attributes ]
del self.__dict__['sys']
del self.__dict__['unittest']
del self.__dict__['attribute']
del self.__dict__['TESTCASE']
del self.__dict__['self']
