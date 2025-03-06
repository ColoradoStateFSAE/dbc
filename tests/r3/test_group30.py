from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group30(BaseTest):
    file = "r3.dbc"
    id = 0x3EA
    signal_count = 4

    def test_gearbox_line_pressure(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/10,
                offset=-101.3
            ),
            minimum=None,
            maximum=None,
            unit="kPa"
        )

    def test_injection_stage_3_duty_cycle(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
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

    def test_injection_stage_4_duty_cycle(self):
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
            unit="%"
        )

    def test_crank_case_pressure(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=55,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/10,
                offset=-101.3
            ),
            minimum=None,
            maximum=None,
            unit="kPa"
        )
