from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group46(BaseTest):
    file = "r3.dbc"
    id = 0x477
    signal_count = 7

    def test_engine_limiter_max_rpm(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="RPM"
        )

    def test_cut_percentage(self):
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

    def test_engine_limiter_function(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
            length=8,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="enum"
        )

    def test_rpm_limiter_function(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=47,
            length=8,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="enum"
        )

    def test_cut_percentage_function(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=55,
            length=8,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="enum"
        )

    def test_engine_limiter_method(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=63,
            length=4,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="enum"
        )

    def test_rpm_limiter_method(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=59,
            length=4,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="enum"
        )
