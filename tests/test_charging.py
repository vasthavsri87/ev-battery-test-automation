from battery.battery_controller import BatteryController


def test_charging_starts_when_battery_not_full():

    battery = BatteryController(50)

    result = battery.start_charging()

    assert result is True


def test_charging_stops_at_full_battery():

    battery = BatteryController(100)

    result = battery.start_charging()

    assert result is False