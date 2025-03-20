from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group26(BaseTest):
    file = "r3.dbc"
    id = 0x3E6
    signal_count = 4

    def test_nos_pressure_sensor_2(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=11/50,
                offset=-101.3
            ),
            minimum=None,
            maximum=None,
            unit="kPa"
        )

    def test_nos_pressure_sensor_3(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=11/50,
                offset=-101.3
            ),
            minimum=None,
            maximum=None,
            unit="kPa"
        )

    def test_nos_pressure_sensor_4(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=11/50,
                offset=-101.3
            ),
            minimum=None,
            maximum=None,
            unit="kPa"
        )

    def test_turbo_speed_sensor_2(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=55,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=10,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="RPM"
        )
