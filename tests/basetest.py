import unittest
import cantools
import inspect
import re
import warnings

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

class BaseTest(unittest.TestCase):
    file = None
    id = None
    signal_count = None
    expected = None
    test_count = 0

    @classmethod
    def setUpClass(cls):
        if cls.file is None:
            raise RuntimeError("'file' must be set")
        
        if cls.signal_count is None:
            raise ValueError("'signal_count' must be set")

        pattern = r"Test_.+"

        if not re.fullmatch(pattern, cls.__name__):
            raise RuntimeError(f"Test fixture name '{cls.__name__}' must be in the format 'Test_message_name'")

        db = cantools.database.load_file(cls.file)
        cls.message=db.get_message_by_name(cls.__name__[5:])
        assert cls.message.frame_id == cls.id
        assert len(cls.message.signals) == cls.signal_count

    @classmethod
    def tearDownClass(cls):
        if(cls.signal_count != cls.test_count):
            warn = "\033[33m"
            reset = "\033[0m"
            print(warn + f"\n{cls.__name__}: found {cls.test_count} tests but expected {cls.signal_count}" + reset)

    def tearDown(self):
        self.__class__.test_count += 1
        
        if self.expected is None:
            raise ValueError("'expected' must be set")
        
        actual = None
        for signal in self.message.signals:
            if(signal.name == self.expected.name):
                actual = signal
                break

        if(actual == None):
            raise RuntimeError(f"Could not find signal '{self.expected.name}' in message '{self.message.name}'")
        
        compare_signals(actual, self.expected)

    def signal_name(self):
        name = inspect.currentframe().f_back.f_code.co_name

        if(name[:5] != "test_"):
            raise RuntimeError(f"Test name '{name}' must start with 'test_'")
        
        return name[5:]

    