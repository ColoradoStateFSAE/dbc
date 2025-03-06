from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group05(BaseTest):
    file = "r3.dbc"
    id = 0x368
    signal_count = 4

    def test_wideband_sensor_1(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=self.signal_name(),
            start=-1+8,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/1000,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="Lambda"
        )

    def test_wideband_sensor_2(self):
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=self.signal_name(),
            start=-1+24,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/1000,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="Lambda"
        )

    def test_wideband_sensor_3(self):
        self.actual = self.message.signals[2]

        self.expected = Signal(
            name=self.signal_name(),
            start=-1+40,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/1000,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="Lambda"
        )

    def test_wideband_sensor_4(self):
        self.actual = self.message.signals[3]

        self.expected = Signal(
            name=self.signal_name(),
            start=55,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/1000,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="Lambda"
        )
