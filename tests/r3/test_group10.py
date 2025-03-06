from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group10(BaseTest):
    file = "r3.dbc"
    id = 0x36D
    signal_count = 2

    def test_exhaust_cam_angle_1(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=self.signal_name(),
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
            unit="°"
        )

    def test_exhaust_cam_angle_2(self):
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=self.signal_name(),
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
            unit="°"
        )
