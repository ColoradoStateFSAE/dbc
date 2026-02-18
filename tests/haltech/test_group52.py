from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group52(BaseTest):
    file = "dbc/haltech.dbc"
    id = 0x6F6
    signal_count = 2
    cycle_time = 1000/5

    def test_total_fuel_used_since_trip_1_reset(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=32,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="cc"
        )
    
    def test_trip_meter_1(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
            length=32,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="m"
        )
