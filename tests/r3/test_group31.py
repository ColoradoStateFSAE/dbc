from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group31(BaseTest):
    file = "r3.dbc"
    id = 0x3EB
    signal_count = 3

    def test_race_timer(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=32,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="ms"
        )

    def test_ignition_angle_bank_1(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
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

    def test_ignition_angle_bank_2(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=55,
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
