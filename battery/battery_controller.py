class BatteryController:

    def __init__(self, battery_level=50, temperature=25):
        self.battery_level = battery_level
        self.temperature = temperature
        self.charging = False

    def get_battery_level(self):
        return self.battery_level

    def get_temperature(self):
        return self.temperature

    def start_charging(self):
        if self.battery_level >= 100:
            return False

        self.charging = True
        return True

    def charge(self):
        if self.charging and self.battery_level < 100:
            self.battery_level += 10

        if self.battery_level > 100:
            self.battery_level = 100

    def stop_charging(self):
        self.charging = False

    def is_overheated(self):
        return self.temperature > 60