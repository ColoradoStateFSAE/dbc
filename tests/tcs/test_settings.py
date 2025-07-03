from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_settings(BaseTest):
    file = "tcs.dbc"
    id = 0x102
    signal_count = 8

    def test_start_point(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=12,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="microseconds"
        )

    def test_end_point(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
            length=12,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="microseconds"
        )

    def test_friction_point(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
            length=12,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="microseconds"
        )

    def test_auto_shift(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=55,
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
        
    def test_set_start_point(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=59,
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
        
    def test_set_end_point(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=58,
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
        
        
    def test_set_friction_point(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=57,
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
        
    def test_set_auto_shift(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=56,
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