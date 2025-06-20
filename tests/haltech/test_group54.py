from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group54(BaseTest):
    file = "haltech.dbc"
    id = 0x6F8
    signal_count = 5

    def test_exhaust_cutout_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=8,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="enum"
        )

    def test_nitrous_bottle_opener_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=15,
            length=8,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="enum"
        )

    def test_gen_open_loop_mtr_cntrl_1_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
            length=8,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="enum"
        )

    def test_gen_open_loop_mtr_cntrl_2_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=31,
            length=8,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="enum"
        )

    def test_gen_open_loop_mtr_cntrl_3_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
            length=8,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="enum"
        )
