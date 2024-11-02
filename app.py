from flask import Flask, render_template, request, jsonify
from controller import HomeController

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

if __name__ == '__main__':
    app.run(debug=True)