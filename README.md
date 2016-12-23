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
