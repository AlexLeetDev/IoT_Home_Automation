# IoT Home Automation

![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue) ![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Active-success)

A 🌐 Flask-based IoT home automation dashboard that allows users to control and monitor various smart home devices like lights, thermostats, and door locks through a user-friendly web interface.

## ⚙️ Features

- 🏡 **Thermostat Control**: Set and view target temperature.
- 💡 **Light Control**: Toggle lights on and off.
- 🔒 **Door Lock Control**: Lock and unlock doors remotely.
- 📊 **Real-Time Status Updates**: View the current status of all devices on the dashboard.

## 🛠️ Technologies Used

- **Backend**: &nbsp;![Python](https://img.shields.io/badge/Python-3.7%2B-blue) &nbsp; ![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue)
- **Frontend**: HTML, CSS, JavaScript (AJAX for seamless updates)
- **Device Control**: MVC structure with a controller managing all device interactions

## 🚀 Getting Started

## 📁 Project Structure

The project is organized as follows:

```plaintext
IoT_Home_Automation/
├── app.py              # Main application file with Flask routes
├── controller.py       # Controller to manage device interactions
├── devices/            # Device modules for different IoT functionalities
│   ├── door_lock.py    # Door lock control
│   ├── light.py        # Light control
│   └── thermostat.py   # Thermostat control
├── templates/          # HTML templates for the app
│   └── index.html      # Main dashboard interface
├── static/             # Static files (CSS, JavaScript)
│   └── style.css       # Custom styling for the dashboard
├── venv/               # Virtual environment (not tracked in Git)
└── requirements.txt    # List of dependencies for the project

## 🖥️ Usage

Once the application is running, you can use the IoT Home Automation dashboard to interact with connected devices. Here’s how each feature works:

- **Adjust Thermostat**:
  - Set a desired target temperature for your thermostat by entering a value and clicking the "Adjust" button.
  - The dashboard will display both the current temperature and your target setting.

- **Toggle Light**:
  - Click the "Toggle Light" button to switch the light on or off.
  - The current status of the light (On/Off) is displayed on the dashboard.

- **Toggle Door Lock**:
  - Click the "Toggle Door Lock" button to lock or unlock the door.
  - The dashboard will show the door’s current state (Locked/Unlocked).

Each control action sends a request to the backend, which updates the device status in real-time. This enables easy and convenient management of your smart home devices from a single interface.
