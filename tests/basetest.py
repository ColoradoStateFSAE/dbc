import unittest
import cantools

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
    name = None
    id = None
    signal_count = None
    expected = None
    actual = None

    @classmethod
    def setUpClass(cls):
        if cls.file is None:
            raise RuntimeError("'file' must be set")

        if cls.name is None:
            raise ValueError("'name' must be set")
        
        if cls.signal_count is None:
            raise ValueError("'signal_count' must be set")

        db = cantools.database.load_file(cls.file)
        cls.message=db.get_message_by_name(cls.name)
        assert cls.message.frame_id == cls.id
        assert len(cls.message.signals) == cls.signal_count

    def tearDown(self):
        if self.actual is None:
            raise RuntimeError("'actual' must be set")

        if self.expected is None:
            raise ValueError("'expected' must be set")
        
        compare_signals(self.actual, self.expected)

    