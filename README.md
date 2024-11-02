# IoT Home Automation

![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue) ![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Active-success)

A 🌐 Flask-based IoT home automation dashboard that allows users to control and monitor various smart home devices like lights, thermostats, and door locks through a user-friendly web interface.

---

## ⚙️ Features

- 🏡 **Thermostat Control**: Set and view target temperature.
- 💡 **Light Control**: Toggle lights on and off.
- 🔒 **Door Lock Control**: Lock and unlock doors remotely.
- 📊 **Real-Time Status Updates**: View the current status of all devices on the dashboard.

---

## 🛠️ Technologies Used

- ![Python](https://img.shields.io/badge/Python-3.7%2B-blue)&nbsp;&nbsp;
  The programming language used to build the backend of the application, allowing communication between the web server and smart devices.
- ![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue)&nbsp;&nbsp;
  A simple web framework that helps create the web server and manage user requests from the interface.
- ![MySQL](https://img.shields.io/badge/MySQL-8.0.39-blue)&nbsp;&nbsp;
  A database system used to store logs of device actions and track history. It keeps records of what devices do over time.

- **Frontend Technologies**:
  HTML, CSS, JavaScript (with AJAX for smooth updates)
  These are used to create the user interface of the application, making it easy for users to interact with their smart devices.

- **Device Control Architecture**:
  Uses a Model-View-Controller (MVC) design to manage how devices are controlled and how information is displayed, keeping things organized and efficient.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7** or later
- **MySQL** server for logging device interactions
- Required Python packages listed in `requirements.txt`

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/AlexLeetDev/IoT_Home_Automation.git
   cd IoT_Home_Automation
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

### Database Configuration

1. **Start your MySQL server**.
2. **Create the necessary database and tables**:

   ```sql
   CREATE DATABASE iot_home_automation;
   USE iot_home_automation;

   CREATE TABLE Devices (  
       device_id INT AUTO_INCREMENT PRIMARY KEY,  
       device_name VARCHAR(255),  
       device_type VARCHAR(255),  
       location VARCHAR(255),  
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
   );

   CREATE TABLE EventLogs (  
       log_id INT AUTO_INCREMENT PRIMARY KEY,  
       device_id INT,  
       event_type VARCHAR(255),  
       event_value VARCHAR(255),  
       event_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
       FOREIGN KEY (device_id) REFERENCES Devices(device_id)  
   );
   ```

3. **Configure MySQL connection in your project files**.

   Update the connection settings directly within each device file:

   ```python
   db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="iot_home_automation"
   )
   ```

---

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
```

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
