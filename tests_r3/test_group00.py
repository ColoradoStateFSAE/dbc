import unittest
import cantools
from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import util

db = cantools.database.load_file("r3.dbc")
message = db.get_message_by_name("group00")

class TestGroup00(unittest.TestCase):
    def tearDown(self):
        util.compare_signals(self.actual, self.expected)

    def test_rpm(self):
        self.actual = message.signals[0]

        self.expected = Signal(
            name="rpm",
            start=-1+8,
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

    def test_manifold_pressure(self):
        self.actual = message.signals[1]

        self.expected = Signal(
            name="manifold_pressure",
            start=-1+24,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="kPa (Abs)",
        )

    def test_throttle_position(self):
        self.actual = message.signals[2]

        self.expected = Signal(
            name="throttle_position",
            start=-1+40,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="%",
        )

    def test_coolant_pressure(self):
        self.actual = message.signals[3]

        self.expected = Signal(
            name="coolant_pressure",
            start=-1+56,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=-101.3
            ),
            minimum=None,
            maximum=None,
            unit="kPa",
        )

if __name__ == '__main__':
    unittest.main()
