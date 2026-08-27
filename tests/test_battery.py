import pytest

from battery.battery_controller import BatteryController


def test_battery_level_is_valid():

    battery = BatteryController(50)

    assert 0 <= battery.get_battery_level() <= 100


def test_charging_increases_battery():

    battery = BatteryController(50)

    battery.start_charging()
    battery.charge()

    assert battery.get_battery_level() == 60


def test_battery_does_not_exceed_100():

    battery = BatteryController(95)

    battery.start_charging()
    battery.charge()

    assert battery.get_battery_level() <= 100


@pytest.mark.parametrize(
    "battery_level",
    [0, 10, 25, 50, 75, 100]
)
def test_valid_battery_values(battery_level):

    battery = BatteryController(battery_level)

    assert 0 <= battery.get_battery_level() <= 100
def test_overheating_detection():

    battery = BatteryController(50, temperature=70)

    assert battery.is_overheated() is True