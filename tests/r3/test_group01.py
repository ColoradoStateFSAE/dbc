from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import inspect
from tests.basetest import BaseTest
class TestGroup01(BaseTest):
    name = "group01"
    id = 0x361
    file = "r3.dbc"

    def test_fuel_pressure(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+8,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=-101.3
            ),
            minimum=None,
            maximum=None,
            unit="kPa",
        )

    def test_oil_pressure(self):
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+24,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=-101.3
            ),
            minimum=None,
            maximum=None,
            unit="kPa",
        )

    def test_engine_demand(self):
        self.actual = self.message.signals[2]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+40,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="%",
        )

    def test_wastegate_pressure(self):
        self.actual = self.message.signals[3]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+56,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.1,
                offset=-101.3
            ),
            minimum=None,
            maximum=None,
            unit="kPa",
        )
