from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_set_status(BaseTest):
    file = "tcs.dbc"
    id = 0x65D
    signal_count = 3

    def test_antistall(self):
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
            unit=None
        )

    def test_rpm_limiter(self):
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
            unit=None
        )

    def test_over_rev(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=5,
            length=1,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit=None
        )
    