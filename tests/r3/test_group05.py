from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
import inspect
from tests.basetest import BaseTest

class TestGroup05(BaseTest):
    name = "group05"
    id = 0x368
    file = "r3.dbc"

    def test_wideband_sensor_1(self):
        self.actual = self.message.signals[0]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+8,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.001,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="Lambda",
        )

    def test_wideband_sensor_2(self):
        self.actual = self.message.signals[1]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+24,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.001,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="Lambda",
        )

    def test_wideband_sensor_3(self):
        self.actual = self.message.signals[2]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+40,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.001,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="Lambda",
        )

    def test_wideband_sensor_4(self):
        self.actual = self.message.signals[3]

        self.expected = Signal(
            name=inspect.currentframe().f_code.co_name[5:],
            start=-1+56,
            length=16,
            byte_order="big_endian",
            is_signed=False,
            conversion=BaseConversion.factory(
                scale=0.001,
                offset=0
            ),
            minimum=None,
            maximum=None,
            unit="Lambda",
        )
