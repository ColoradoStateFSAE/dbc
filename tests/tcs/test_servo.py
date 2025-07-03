from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_servo(BaseTest):
    file = "tcs.dbc"
    id = 0x100
    signal_count = 3

    def test_servo_position(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=12,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="microseconds"
        )

    def test_servo_percentage(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="%"
        )
        
    def test_set_servo_position(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=8,
            length=1,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="boolean"
        )