import unittest
import cantools
import inspect
import re

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
    actual = None
    expected = None

    @classmethod
    def setUpClass(cls):
        if cls.file is None:
            raise RuntimeError("'file' must be set")
        
        if cls.signal_count is None:
            raise ValueError("'signal_count' must be set")

        db = cantools.database.load_file(cls.file)

        pattern = r"Test_.+"
        name = cls.__name__

        if not re.fullmatch(pattern, name):
            raise RuntimeError(f"Test fixture name '{name}' must be in the format 'Test_message_name'")
        
        name = name[5:]

        cls.message=db.get_message_by_name(name)
        assert cls.message.frame_id == cls.id
        assert len(cls.message.signals) == cls.signal_count
        
    def tearDown(self):
        if self.actual is None:
            raise RuntimeError("'actual' must be set")

        if self.expected is None:
            raise ValueError("'expected' must be set")
        
        compare_signals(self.actual, self.expected)

    def signal_name(self):
        name = inspect.currentframe().f_back.f_code.co_name

        if(name[:5] != "test_"):
            raise RuntimeError(f"Test name '{name}' must start with 'test_'")
        
        return name[5:]

    