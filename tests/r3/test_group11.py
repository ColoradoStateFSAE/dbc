from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import inspect
from tests.basetest import BaseTest

class TestGroup11(BaseTest):
    name = "group11"
    id = 0x36E
    signal_count = 4
    file = "r3.dbc"

    def test_engine_limiting_active(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
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
            unit="boolean",
        )

    def test_launch_control_ignition_retard(self):
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+24,
            length=16,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1/10,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="°",
        )

    def test_launch_control_fuel_enrich(self):
        self.actual = self.message.signals[2]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+40,
            length=16,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1/10,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="%",
        )

    def test_longitudinal_g(self):
        self.actual = self.message.signals[3]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+56,
            length=16,
            byte_order="big_endian",
            is_signed=True,
            conversion=BaseConversion.factory(
                scale=1/10,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="m/s2",
        )
