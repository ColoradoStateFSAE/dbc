from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_io12a_avi(BaseTest):
    file = "dbc/haltech.dbc"
    id = 0x2C0
    signal_count = 4
    cycle_time = 20

    def test_avi1_voltage(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=3,
            length=12,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.00122100122100122,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="V"
        )

    def test_avi2_voltage(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=19,
            length=12,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.00122100122100122,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="V"
        )

    def test_avi3_voltage(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=35,
            length=12,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.00122100122100122,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="V"
        )

    def test_avi4_voltage(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=51,
            length=12,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.00122100122100122,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="V"
        )
