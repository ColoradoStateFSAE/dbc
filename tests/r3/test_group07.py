from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import inspect
from tests.basetest import BaseTest

class TestGroup07(BaseTest):
    name = "group07"
    id = 0x36A
    signal_count = 2
    file = "r3.dbc"

    def test_knock_level_1(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+8,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/100,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="dB",
        )

    def test_knock_level_2(self):
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+24,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/100,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="dB",
        )
