import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    haltech_suite = loader.discover("tests/haltech")

    runner = unittest.TextTestRunner()
    runner.run(haltech_suite)
