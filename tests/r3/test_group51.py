from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group51(BaseTest):
    file = "r3.dbc"
    id = 0x6F4
    signal_count = 5

    def test_park_light_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=0,
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
    
    def test_head_light_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=1,
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
    
    def test_high_beam_light_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=2,
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
    
    def test_left_indicator_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=3,
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
    
    def test_right_indicator_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=4,
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
