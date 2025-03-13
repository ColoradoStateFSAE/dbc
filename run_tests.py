import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    haltech_suite = loader.discover("tests/r3")
    tcs_suite = loader.discover("tests/tcs")

    runner = unittest.TextTestRunner()
    runner.run(haltech_suite)
    runner.run(tcs_suite)
