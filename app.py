from flask import Flask, render_template, request, jsonify
from controller import HomeController
import mysql.connector

# Initialize Flask app and the HomeController
app = Flask(__name__)
controller = HomeController()

@app.route('/')
def home():
    """Render the main dashboard with device statuses."""
    statuses = controller.get_status()  # Get status of all devices
    return render_template("index.html", statuses=statuses)

@app.route('/adjust_thermostat', methods=["POST"])
def adjust_thermostat():
    """Route to adjust thermostat target temperature."""
    data = request.get_json()
    new_temp = float(data.get("temperature"))
    controller.thermostat.adjust_temperature(new_temp)
    return jsonify({"target_temp": controller.thermostat.target_temp})

@app.route('/toggle_light', methods=["POST"])
def toggle_light():
    """Route to toggle the light on/off."""
    controller.light.toggle()  # Toggle light on or off
    return jsonify({"is_on": controller.light.is_on})

@app.route('/toggle_door', methods=["POST"])
def toggle_door():
    """Route to lock/unlock the door."""
    controller.door_lock.toggle()  # Toggle door lock state
    return jsonify({"is_locked": controller.door_lock.is_locked})

@app.route('/logs')
def view_logs():
    """Route to view event logs from the database."""
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="5eDL0@z2tK68",
        database="iot_home_automation"
    )
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM EventLogs ORDER BY event_timestamp DESC")
    logs = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("logs.html", logs=logs)  # Pass logs to the logs.html template

if __name__ == '__main__':
    app.run(debug=True)
