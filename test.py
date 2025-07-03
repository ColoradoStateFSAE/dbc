import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    haltech_suite = loader.discover("tests/haltech")
    tcs_suite = loader.discover("tests/tcs")
    tcs_suite = loader.discover("tests/swc")

    runner = unittest.TextTestRunner()
    runner.run(haltech_suite)
    runner.run(tcs_suite)
