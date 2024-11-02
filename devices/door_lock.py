 # door_lock.py

import mysql.connector

class DoorLock:
    def __init__(self):
        self.is_locked = True

    def log_event(self, event_type, event_value):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="5eDL0@z2tK68",
            database="iot_home_automation"
        )
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO EventLogs (device_id, event_type, event_value) VALUES (%s, %s, %s)",
            (1, event_type, event_value)
        )
        db.commit()
        cursor.close()
        db.close()

    def toggle(self):
        """Toggle door lock state."""
        self.is_locked = not self.is_locked
        print(f"Door is now {'locked' if self.is_locked else 'unlocked'}")

    def get_status(self):
        """Return the door lock's current state."""
        return {"is_locked": self.is_locked}
