 # door_lock.py
class DoorLock:
    def __init__(self):
        self.is_locked = True

    def toggle(self):
        """Toggle door lock state."""
        self.is_locked = not self.is_locked
        print(f"Door is now {'locked' if self.is_locked else 'unlocked'}")

    def get_status(self):
        """Return the door lock's current state."""
        return {"is_locked": self.is_locked}
