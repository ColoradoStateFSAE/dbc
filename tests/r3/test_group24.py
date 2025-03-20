from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group24(BaseTest):
    file = "r3.dbc"
    id = 0x3E4
    signal_count = 28

    def test_neutral_switch(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=15,
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

    def test_reverse_switch(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=14,
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

    def test_gear_switch(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=13,
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

    def test_decel_cut_active(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=12,
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

    def test_transient_throttle_active(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=11,
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

    def test_brake_pedal_switch(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=10,
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

    def test_clutch_switch(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=9,
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

    def test_oil_pressure_light(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=8,
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

    def test_launch_control_active(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
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

    def test_launch_control_switch(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=22,
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

    def test_aux_rpm_limiter_active(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=21,
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

    def test_flat_shift_switch(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=19,
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

    def test_torque_reduction_active(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=17,
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

    def test_traction_control_enabled(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=31,
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

    def test_traction_control_active(self):
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
            unit="boolean"
        )

    def test_air_con_request(self):
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
            unit="boolean"
        )

    def test_air_con_output(self):
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

    def test_thermo_fan_4_on(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=27,
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

    def test_thermo_fan_3_on(self):
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
            unit="boolean"
        )

    def test_thermo_fan_2_on(self):
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
            unit="boolean"
        )

    def test_thermo_fan_1_on(self):
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
            unit="boolean"
        )

    def test_rotary_trim_pot_1(self):
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
            unit="raw"
        )

    def test_rotary_trim_pot_2(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=47,
            length=8,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="raw"
        )

    def test_rotary_trim_pot_3(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=55,
            length=8,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="raw"
        )

    def test_check_engine_light(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=63,
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

    def test_battery_light_active(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=62,
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

    def test_hand_brake_state(self):
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

    def test_traction_control_light(self):
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
