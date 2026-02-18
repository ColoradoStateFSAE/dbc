from cantools.database.can.signal import Signal
from cantools.database.conversion import BaseConversion
from tests.basetest import BaseTest

class Test_group33(BaseTest):
    file = "dbc/haltech.dbc"
    id = 0x3ED
    signal_count = 1
    cycle_time = 1000/50

    def test_torque_management_combined_ignition_correction(self):
        self.expected = Signal(
            name=self.signal_name(),
            start=7,
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
