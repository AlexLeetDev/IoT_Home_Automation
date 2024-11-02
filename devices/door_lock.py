import mysql.connector

class DoorLock:
    def __init__(self):
        self.is_locked = True

    def log_event(self, event_type, event_value):
        print(f"Logging event: {event_type} with value: {event_value}")  # Debugging statement
        try:
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
            print("Event logged successfully")
            cursor.close()
            db.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def toggle(self):
        """Toggle door lock state."""
        self.is_locked = not self.is_locked
        status = 'locked' if self.is_locked else 'unlocked'
        print(f"Door is now {status}")
        self.log_event("toggle", status)

    def get_status(self):
        """Return the door lock's current state."""
        return {"is_locked": self.is_locked}
