from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import inspect
from tests.basetest import BaseTest

class TestGroup10(BaseTest):
    name = "group10"
    id = 0x36D
    signal_count = 2
    file = "r3.dbc"

    def test_exhaust_cam_angle_1(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+40,
            length=16,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1/10,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="°",
        )

    def test_exhaust_cam_angle_2(self):
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+56,
            length=16,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1/10,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="°",
        )
