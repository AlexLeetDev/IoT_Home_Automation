import mysql.connector

class Light:
    def __init__(self):
        self.is_on = False

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
                (2, event_type, event_value)
            )
            db.commit()
            print("Event logged successfully")
            cursor.close()
            db.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def toggle(self):
        """Toggle light on or off."""
        self.is_on = not self.is_on
        status = 'on' if self.is_on else 'off'
        print(f"Light turned {status}")
        self.log_event("toggle", status)

    def get_status(self):
        """Return the light's current state."""
        return {"is_on": self.is_on}
