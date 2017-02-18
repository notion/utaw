"""
UTAW - Unit Test Assertion Wrapper.

Wraps the python builtin unittest assertions in a library that doesn't require you to instantiate a TestCase.
"""


# [ Imports ]
from . assertions import (
    assertAlmostEqual,
    assertAlmostEquals,
    assertCountEqual,
    assertDictContainsSubset,
    assertDictEqual,
    assertEqual,
    assertEquals,
    assertFalse,
    assertGreater,
    assertGreaterEqual,
    assertIn,
    assertIs,
    assertIsInstance,
    assertIsNone,
    assertIsNot,
    assertIsNotNone,
    assertLess,
    assertLessEqual,
    assertListEqual,
    assertLogs,
    assertMultiLineEqual,
    assertNotAlmostEqual,
    assertNotAlmostEquals,
    assertNotEqual,
    assertNotEquals,
    assertNotIn,
    assertNotIsInstance,
    assertNotRegex,
    assertNotRegexpMatches,
    assertRaises,
    assertRaisesRegex,
    assertRaisesRegexp,
    assertRegex,
    assertRegexpMatches,
    assertSequenceEqual,
    assertSetEqual,
    assertTrue,
    assertTupleEqual,
    assertWarns,
    assertWarnsRegex,
)
