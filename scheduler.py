# scheduler.py
import schedule
import time
from controller import HomeController

# Initialize the HomeController
controller = HomeController()

# Define Scheduled Tasks

def turn_off_light_at_night():
    """Turn off light every night at 10 PM"""
    if controller.light.is_on:  # Only toggle if the light is currently on
        controller.light.toggle()
    print("Scheduled Task: Light turned off at 10 PM")

def turn_on_light_in_morning():
    """Turn on light every morning at 6 AM"""
    if not controller.light.is_on: # Only toggle if the light is currently off
        controller.light.toggle()
    print("Scheduled Task: Light turned on at 6 AM.")

def adjust_thermostat_morning():
    """Set thermostat to 70°F every morning at 7 AM."""
    controller.thermostat.adjust_temperature(70)
    print("Scheduled Task: Thermostat set to 70°F at 7 AM")

def adjust_thermostat_evening():
    """Set thermostat to 68°F every evening at 8 PM."""
    controller.thermostat.adjust_temperature(68)
    print("Scheduled Task: Thermostat set to 68°F at 8 PM")

# Schedule the tasks
schedule.every().day.at("22.00").do(turn_off_light_at_night)
schedule.every().day.at("06.00").do(turn_on_light_in_morning)
schedule.every().day.at("07.00").do(adjust_thermostat_morning)
schedule.every().day.at("20.00").do(adjust_thermostat_evening)

# Continuously run the scheduler
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
