import unittest
import cantools
from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import util

db = cantools.database.load_file("r3.dbc")
message = db.get_message_by_name("group03")

class TestGroup03(unittest.TestCase):
    def tearDown(self):
        util.compare_signals(self.actual, self.expected)

    def test_wheel_slip(self):
        self.actual = message.signals[0]

        self.expected = Signal(
            name="wheel_slip",
            start=-1+8,
            length=16,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="km/h",
        )

    def test_wheel_diff(self):
        self.actual = message.signals[1]

        self.expected = Signal(
            name="wheel_diff",
            start=-1+24,
            length=16,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="km/h",
        )

    def test_launch_control_end_rpm(self):
        self.actual = message.signals[2]

        self.expected = Signal(
            name="launch_control_end_rpm",
            start=-1+56,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="RPM",
        )

if __name__ == '__main__':
    unittest.main()
