"""
UTAW - Unit Test Assertion Wrapper.

Extract the assertions one by one so that static checkers see them.
"""


# [ Imports ]
import unittest
import sys


# [ Globals ]
# use a real test case because the assertion reporting uses instance methods.
TESTCASE = unittest.TestCase()
# always report the full diff
TESTCASE.maxDiff = None
# vulture
assert not TESTCASE.maxDiff


# [ Add TestCase Assertions ]
# [ -Equality ]
assertEqual = TESTCASE.assertEqual
assertEquals = TESTCASE.assertEquals
assertCountEqual = TESTCASE.assertCountEqual
assertDictEqual = TESTCASE.assertDictEqual
assertListEqual = TESTCASE.assertListEqual
assertSequenceEqual = TESTCASE.assertSequenceEqual
assertSetEqual = TESTCASE.assertSetEqual
assertTupleEqual = TESTCASE.assertTupleEqual
assertMultiLineEqual = TESTCASE.assertMultiLineEqual

# [ -Inequality ]
assertNotEqual = TESTCASE.assertNotEqual
assertNotEquals = TESTCASE.assertNotEquals

# [ -Is-ness ]
assertIs = TESTCASE.assertIs
assertIsNot = TESTCASE.assertIsNot
assertIsInstance = TESTCASE.assertIsInstance
assertNotIsInstance = TESTCASE.assertNotIsInstance
assertIsNone = TESTCASE.assertIsNone
assertIsNotNone = TESTCASE.assertIsNotNone

# [ -Near Equality ]
assertAlmostEqual = TESTCASE.assertAlmostEqual
assertAlmostEquals = TESTCASE.assertAlmostEquals

# [ -Near Inequality ]
assertNotAlmostEqual = TESTCASE.assertNotAlmostEqual
assertNotAlmostEquals = TESTCASE.assertNotAlmostEquals

# [ -Comparison ]
assertGreater = TESTCASE.assertGreater
assertGreaterEqual = TESTCASE.assertGreaterEqual
assertLess = TESTCASE.assertLess
assertLessEqual = TESTCASE.assertLessEqual

# [ -Containment ]
assertDictContainsSubset = TESTCASE.assertDictContainsSubset
assertIn = TESTCASE.assertIn
assertNotIn = TESTCASE.assertNotIn

# [ -Truthiness ]
assertTrue = TESTCASE.assertTrue
assertFalse = TESTCASE.assertFalse

# [ -Logging ]
assertLogs = TESTCASE.assertLogs

# [ -Regex ]
assertRegex = TESTCASE.assertRegex
assertNotRegex = TESTCASE.assertNotRegex
assertRegexpMatches = TESTCASE.assertRegexpMatches
assertNotRegexpMatches = TESTCASE.assertNotRegexpMatches

# [ -Exceptions ]
assertRaises = TESTCASE.assertRaises
assertRaisesRegex = TESTCASE.assertRaisesRegex
assertRaisesRegexp = TESTCASE.assertRaisesRegexp

# [ -Warnings ]
assertWarns = TESTCASE.assertWarns
assertWarnsRegex = TESTCASE.assertWarnsRegex
