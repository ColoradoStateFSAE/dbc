import unittest
import cantools
from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import util

db = cantools.database.load_file("r3.dbc")
message = db.get_message_by_name("group02")

class TestGroup02(unittest.TestCase):
    def tearDown(self):
        util.compare_signals(self.actual, self.expected)
        
    def test_injection_stage_1_duty_cycle(self):
        self.actual = message.signals[0]

        self.expected = Signal(
            name="injection_stage_1_duty_cycle",
            start=-1+8,
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

    def test_injection_stage_2_duty_cycle(self):
        self.actual = message.signals[1]

        self.expected = Signal(
            name="injection_stage_2_duty_cycle",
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
            unit="%",
        )

    def test_ignition_angle_leading(self):
        self.actual = message.signals[2]

        self.expected = Signal(
            name="ignition_angle_leading",
            start=-1+40,
            length=16,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="°",
        )

if __name__ == '__main__':
    unittest.main()
