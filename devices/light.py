 # light.py
class Light:
    def __init__(self):
        self.is_on = False

    def toggle(self):
        """Toggle light on or off."""
        self.is_on = not self.is_on
        print(f"Light turned {'on' if self.is_on else 'off'}")

    def get_status(self):
        """Return the light's current state."""
        return {"is_on": self.is_on}
