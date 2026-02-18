from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group53(BaseTest):
    file = "dbc/haltech.dbc"
    id = 0x6F7
    signal_count = 3
    cycle_time = 1000/10

    def test_generic_output_1_20_states(self):
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
            unit="bit-field"
        )

    def test_calculated_air_temperature(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/10,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="K"
        )

    def test_water_injection_advanced_solenoid_duty_cycle(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=55,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/10,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="%"
        )
