from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group08(BaseTest):
    file = "r3.dbc"
    id = 0x36B
    signal_count = 4

    def test_brake_pressure_front(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=self.signal_name(),
            start=-1+8,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=-101.3
            ),
            minimum=None,
            maximum=None,
            unit="kPa"
        )

    def test_nos_pressure_sensor_1(self):
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=self.signal_name(),
            start=-1+24,
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

    def test_turbo_speed_sensor_1(self):
        self.actual = self.message.signals[2]

        self.expected = Signal(
            name=self.signal_name(),
            start=-1+40,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1*10,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="RPM"
        )

    def test_lateral_g(self):
        self.actual = self.message.signals[3]

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
            unit="m/s2"
        )
