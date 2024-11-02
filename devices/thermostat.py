# thermostat.py 
class Thermostat:
    def __init__(self):
        self.current_temp = 72
        self.target_temp = 72

    def adjust_temperature(self, new_temp):
        """Set a new target temperature."""
        self.target_temp = new_temp
        print(f"Target temperature set to {self.target_temp}°F")

    def get_status(self):
        """Return current and target temperatures."""
        return {
            "current_temp": self.current_temp,
            "target_temp": self.target_temp
        }