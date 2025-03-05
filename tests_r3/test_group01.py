import unittest
import cantools
from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import util

db = cantools.database.load_file("r3.dbc")
message = db.get_message_by_name("group01")

class TestGroup01(unittest.TestCase):
    def tearDown(self):
        util.compare_signals(self.actual, self.expected)

    def test_fuel_pressure(self):
        self.actual = message.signals[0]

        self.expected = Signal(
            name="fuel_pressure",
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
        self.actual = message.signals[1]

        self.expected = Signal(
            name="oil_pressure",
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
        self.actual = message.signals[2]

        self.expected = Signal(
            name="engine_demand",
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
        self.actual = message.signals[3]

        self.expected = Signal(
            name="wastegate_pressure",
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

if __name__ == '__main__':
    unittest.main()
