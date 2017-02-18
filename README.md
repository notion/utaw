UTAW: UnitTest Assertion Wrapper

# What
`UTAW` is a wrapper around the python stdlib's unittest assertion functions.

Python's unittest library has some great built-in assertion functions which provide really nice output and diffs
when assertions fail.

However, they're only accessible as methods for a unittest TestCase object, rather than being exposed by the
library itself.

If you want to use the unittest functions in just bare function tests, you have to do some awkward things, which this
module now hides from you

# Why
This module exists because for various projects I inevitably:
* used plain `assert` statements and eventually regretted the lack of quality output/diffs
* created my own custom assertion commands
* used a variation of this library at the head of every test file (`utaw = unittest.TestCase()`)

# Use
You use this module as you would `self` in a unittest TestCase:
```python
import utaw

def test_lists():
    """Test two lists match."""
    by_hand = [1, 2, 3, 4]
    by_range = list(range(1, 5))
    utaw.assertListEqual(by_hand, by_range)
```

See more examples and what functions are available at [the unittest webpage](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)

# API
Generally, the API will always be updated to follow the latest standard library assertions,
found at [the unittest webpage](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual).
This version supports:

## Equality
* [`assertEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)
* [`assertEquals`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEquals)
* [`assertCountEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertCountEqual)
* [`assertDictEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual)
* [`assertListEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual)
* [`assertSequenceEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual)
* [`assertSetEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSetEqual)
* [`assertTupleEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual)
* [`assertMultiLineEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual)

## Inequality
* [`assertNotEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual)
* [`assertNotEquals`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEquals)

## Is-ness
* [`assertIs`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs)
* [`assertIsNot`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot)
* [`assertIsInstance`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance)
* [`assertNotIsInstance`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance)
* [`assertIsNone`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone)
* [`assertIsNotNone`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone)

## Near Equality
* [`assertAlmostEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual)
* [`assertAlmostEquals`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEquals)

## Near Inequality
* [`assertNotAlmostEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual)
* [`assertNotAlmostEquals`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEquals)

## Comparison
* [`assertGreater`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreater)
* [`assertGreaterEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreaterEqual)
* [`assertLess`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLess)
* [`assertLessEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLessEqual)

## Containment
* [`assertDictContainsSubset`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictContainsSubset)
* [`assertIn`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn)
* [`assertNotIn`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn)

## Truthiness
* [`assertTrue`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue)
* [`assertFalse`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse)

## Logging
* [`assertLogs`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs)

## Regex
* [`assertRegex`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegex)
* [`assertNotRegex`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegex)
* [`assertRegexpMatches`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegexpMatches)
* [`assertNotRegexpMatches`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegexpMatches)

## Exceptions
* [`assertRaises`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)
* [`assertRaisesRegex`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex)
* [`assertRaisesRegexp`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegexp)

## Warnings
* [`assertWarns`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns)
* [`assertWarnsRegex`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex)
