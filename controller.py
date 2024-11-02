# controller.py
from devices.thermostat import Thermostat
from devices.light import Light
from devices.door_lock import DoorLock

class HomeController:
    def __init__(self):
        self.thermostat = Thermostat()
        self.light = Light()
        self.door_lock = DoorLock()

    def get_status(self):
        """Return the status of all devices."""
        return {
            "thermostat": self.thermostat.get_status(),
            "light": self.light.get_status(),
            "door_lock": self.door_lock.get_status() 
        }
