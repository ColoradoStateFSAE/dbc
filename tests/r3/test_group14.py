from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group14(BaseTest):
    file = "r3.dbc"
    id = 0x371
    signal_count = 2

    def test_fuel_flow(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="cc/min"
        )

    def test_fuel_flow_return(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="cc/min"
        )
