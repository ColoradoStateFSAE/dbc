from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group49(BaseTest):
    file = "r3.dbc"
    id = 0x6F2
    signal_count = 4

    def test_front_left_tyre_sensor_battery(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/1000,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="V"
        )

    def test_front_right_tyre_sensor_battery(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/1000,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="V"
        )

    def test_rear_left_tyre_sensor_battery(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/1000,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="V"
        )

    def test_rear_right_tyre_sensor_battery(self):
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
            unit="V"
        )
