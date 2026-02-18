from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group07(BaseTest):
    file = "dbc/haltech.dbc"
    id = 0x36A
    signal_count = 2
    cycle_time = 1000/20

    def test_knock_level_1(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/100,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="dB"
        )

    def test_knock_level_2(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/100,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="dB"
        )
