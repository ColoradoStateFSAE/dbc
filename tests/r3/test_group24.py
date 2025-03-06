from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group24(BaseTest):
    file = "r3.dbc"
    id = 0x3E4
    signal_count = 28

    def test_neutral_switch(self):
        self.actual = self.message.signals[0]

        print(self.actual.start)

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
