from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import inspect
from tests.basetest import BaseTest

class TestGroup04(BaseTest):
    name = "group04"
    id = 0x364
    signal_count = 4
    file = "r3.dbc"

    def test_injection_stage_1_average_time(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+8,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.001,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="ms",
        )

    def test_injection_stage_2_average_time(self):
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+24,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.001,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="ms",
        )

    def test_injection_stage_3_average_time(self):
        self.actual = self.message.signals[2]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+40,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.001,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="ms",
        )

    def test_injection_stage_4_average_time(self):
        self.actual = self.message.signals[3]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+56,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.001,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="ms",
        )
