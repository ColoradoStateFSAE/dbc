from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group42(BaseTest):
    file = "r3.dbc"
    id = 0x473
    signal_count = 30

    def test_total_fuel_used(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
            length=32,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="cc"
        )
    
    def test_rolling_antilag_switch_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=39,
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
    
    def test_antilag_switch_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=38,
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
        
    def test_antilag_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=37,
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
        
    def test_traction_control_switch_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=36,
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
        
    def test_primary_fuel_pump_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=35,
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
        
    def test_aux_1_fuel_pump_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=34,
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
        
    def test_aux_2_fuel_pump_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=33,
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
        
    def test_aux_3_fuel_pump_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=32,
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
        
    def test_nitrous_enable_1_switch_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=47,
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
        
    def test_nitrous_enable_1_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=46,
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
        
    def test_nitrous_enable_2_switch_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=45,
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
        
    def test_nitrous_enable_2_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=44,
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
        
    def test_nitrous_enable_3_switch_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=43,
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
        
    def test_nitrous_enable_3_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=42,
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
        
    def test_nitrous_enable_4_switch_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=41,
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
        
    def test_nitrous_enable_4_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=40,
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
        
    def test_nitrous_override_1_switch_state(self):
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
        
    def test_nitrous_override_1_output_state(self):
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
        
    def test_nitrous_override_2_switch_state(self):
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
        
    def test_nitrous_override_2_output_state(self):
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
        
    def test_nitrous_override_3_switch_state(self):
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
        
    def test_nitrous_override_3_output_state(self):
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
        
    def test_nitrous_override_4_switch_state(self):
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
        
    def test_nitrous_override_4_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=48,
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
        
    def test_water_inj_adv_en_switch_state(self):
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
        
    def test_water_inj_adv_en_output_state(self):
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
        
    def test_water_inj_adv_ovr_switch_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=61,
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
        
    def test_water_inj_adv_ovr_output_state(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=60,
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
        
    def test_cut_percentage_method(self):
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
        