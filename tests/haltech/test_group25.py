from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group25(BaseTest):
    file = "haltech.dbc"
    id = 0x3E5
    signal_count = 11

    def test_ignition_switch(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=8,
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

    def test_turbo_timer_time_remaining(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=15,
            length=8,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="s"
        )

    def test_turbo_timer_engine_time_remain(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
            length=8,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="s"
        )

    def test_pit_lane_speed_limiter_error(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=30,
            length=1,
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

    def test_pit_lane_speed_limiter_active(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=29,
            length=1,
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

    def test_pit_lane_speed_limiter_switch(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=28,
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

    def test_abs_error(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=26,
            length=1,
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

    def test_abs_active(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=25,
            length=1,
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

    def test_abs_armed(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=24,
            length=1,
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

    def test_steering_wheel_angle(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
            length=16,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1/10,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="°"
        )

    def test_driveshaft_rpm(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=55,
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
