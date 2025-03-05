import unittest

def compare_signals(actual, expected):
    assert actual.name == expected.name
    assert actual.start == expected.start
    assert actual.length == expected.length
    assert actual.byte_order == expected.byte_order
    assert actual.is_signed == expected.is_signed
    assert actual.conversion.scale == expected.conversion.scale
    assert actual.conversion.offset == expected.conversion.offset
    assert actual.minimum == expected.minimum
    assert actual.maximum == expected.maximum
    assert actual.unit == expected.unit

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("tests_r3")

    runner = unittest.TextTestRunner()
    runner.run(suite)
