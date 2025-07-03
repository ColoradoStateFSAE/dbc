from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_status(BaseTest):
    file = "tcs.dbc"
    id = 0x101
    signal_count = 2
    
    def test_over_rev(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=1,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="boolean"
        )

    def test_antistall(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=6,
            length=1,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="boolean"
        )