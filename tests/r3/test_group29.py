from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group29(BaseTest):
    file = "r3.dbc"
    id = 0x3E9
    signal_count = 11

    def test_generic_sensor_9(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=None,
            minimum=None,
            maximum=None,
            unit=None
        )

    def test_generic_sensor_10(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=None,
            minimum=None,
            maximum=None,
            unit=None
        )

    def test_target_lambda(self):
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
            unit="Lambda"
        )
