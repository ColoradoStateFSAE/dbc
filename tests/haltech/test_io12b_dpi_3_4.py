from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_io12b_dpi_3_4(BaseTest):
    file = "dbc/haltech.dbc"
    id = 0x2C5
    signal_count = 4
    cycle_time = 20

    def test_dpi3_duty_cycle(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=10,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="%"
        )

    def test_dpi3_period(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=8,
            length=17,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.01,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="ms"
        )

    def test_dpi4_duty_cycle(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
            length=10,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="%"
        )

    def test_dpi4_period(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=40,
            length=17,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.01,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="ms"
        )
