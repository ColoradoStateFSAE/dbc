import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("tests_r3")

    runner = unittest.TextTestRunner()
    runner.run(suite)
