import unittest
import cantools
from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import run_tests

class TestGroup01(unittest.TestCase):
    db = None

    def setUp(self):
        if(self.db == None):
            self.db = cantools.database.load_file("r3.dbc")

        self.message = self.db.get_message_by_name("group01")

    def test_fuel_pressure(self):
        run_tests.compare_signals(
            self.message.signals[0],
            Signal(
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
        )

    def test_oil_pressure(self):
        run_tests.compare_signals(
            self.message.signals[1],
            Signal(
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
        )

    def test_engine_demand(self):
        run_tests.compare_signals(
            self.message.signals[2],
            Signal(
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
        )

    def test_coolant_pressure(self):
        run_tests.compare_signals(
            self.message.signals[3],
            Signal(
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
        )

if __name__ == '__main__':
    unittest.main()
