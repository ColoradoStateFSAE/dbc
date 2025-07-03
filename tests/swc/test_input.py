from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_input(BaseTest):
    file = "swc.dbc"
    id = 0x200
    signal_count = 6
    
    def test_up(self):
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

    def test_down(self):
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

    def test_clutch_left(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=15,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.01,
                offset=0
            ),
            minimum=0,
            maximum=100,
            unit="%"
        )

    def test_clutch_right(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=31,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.01,
                offset=0
            ),
            minimum=0,
            maximum=100,
            unit="%"
        )
        
    def test_clutch_left_raw(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=47,
            length=12,
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

    def test_clutch_right_raw(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=51,
            length=12,
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
