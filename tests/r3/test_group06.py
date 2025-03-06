from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group06(BaseTest):
    file = "r3.dbc"
    id = 0x369
    signal_count = 3

    def test_trigger_system_error_count(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=self.signal_name(),
            start=-1+8,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="raw"
        )

    def test_trigger_counter(self):
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=self.signal_name(),
            start=-1+24,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="raw"
        )

    def test_trigger_sync_level(self):
        self.actual = self.message.signals[2]

        self.expected = Signal(
            name=self.signal_name(),
            start=-1+56,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="raw"
        )
