import mysql.connector

class Thermostat:
    def __init__(self):
        self.current_temp = 72
        self.target_temp = 72

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
                (3, event_type, event_value)
            )
            db.commit()
            print("Event logged successfully")
            cursor.close()
            db.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def adjust_temperature(self, new_temp):
        """Set a new target temperature."""
        self.target_temp = new_temp
        print(f"Target temperature set to {self.target_temp}°F")
        self.log_event("adjust", f"Set to {self.target_temp}°F")

    def get_status(self):
        """Return current and target temperatures."""
        return {
            "current_temp": self.current_temp,
            "target_temp": self.target_temp
        }
