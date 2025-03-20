from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group29(BaseTest):
    file = "r3.dbc"
    id = 0x3E9
    signal_count = 11

    def test_generic_sensor_9(self):
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
            unit=None
        )

    def test_generic_sensor_10(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=23,
            length=16,
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

    def test_target_lambda(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1/1000,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="Lambda"
        )

    def test_nitrous_stage_1_output_state(self):
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

    def test_nitrous_stage_2_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=54,
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
        
    def test_nitrous_stage_3_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=53,
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
        
    def test_nitrous_stage_4_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=52,
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
        
    def test_nitrous_stage_5_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=51,
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
        
    def test_nitrous_stage_6_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=50,
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
        
    def test_water_injection_adv_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=49,
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
        
    def test_torque_management_knob(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=63,
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
        
