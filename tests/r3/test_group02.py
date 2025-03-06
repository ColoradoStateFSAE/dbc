from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import inspect
from tests.basetest import BaseTest

class TestGroup02(BaseTest):
    name = "group02"
    id = 0x362
    signal_count = 3
    file = "r3.dbc"
        
    def test_injection_stage_1_duty_cycle(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
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
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
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
        self.actual = self.message.signals[2]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
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
