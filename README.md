# WS25_Prak_YutongXie

## Project Overview

This project aims to implement an automated soil moisture monitoring and irrigation system by integrating hardware devices, embedded-side code, service communication, workflow orchestration, and a user interface into one complete project. The system mainly consists of a soil moisture sensor, an Orange Pi, services deployed on Lehre, CPEE workflow models, robot-related programs, and a front-end interface.

## Project Workflow

The core implementation of this project is a complete communication workflow for soil moisture data, spanning from the Orange Pi to Lehre and finally to CPEE.

First, the soil moisture sensor data is collected on the Orange Pi, where the corresponding service interface is also implemented. Since Lehre cannot directly access the Pi because it is located within a private network, port `18080` on the Orange Pi was forwarded to Lehre. This enabled Lehre to access the data interface hosted on the Orange Pi, allowing CPEE to send requests to the Orange Pi via Lehre and retrieve the current soil moisture status.

Instead of adopting a continuous periodic data-pushing mechanism, this project uses an on-demand communication model: the Orange Pi reads and transmits the current data only when a request is issued by CPEE. This approach avoids unnecessary repeated transmissions and reduces overall system resource consumption.

## Repository Structure

This repository contains the main components of the automatic plant watering system, including the CPEE workflow, robot control programs, the web-based UI, and the sensor interface running on the Orange Pi.

```text
.
├── README.md
├── cpee/
│   └── cpee_process.xml
├── robot_programs/
│   ├── home.urp
│   └── watering.urp
├── lehre_code/
│   ├── humidity.html
│   └── humidity.css
├── orange_pi/
│   └── soil_sensor.py
└── media/
    ├── dry.png
    └── wet.png
```

### Component Overview

| Path | Description |
|---|---|
| `cpee/` | Contains the workflow definition for the automation logic. |
| `cpee/cpee_process.xml` | Defines the full CPEE process, including retrieving soil moisture data, deciding whether the soil is dry or wet, triggering the robot watering action, and updating the UI via `frames_display`. |
| `robot_programs/` | Contains the UR robot programs used for physical actions. |
| `robot_programs/home.urp` | Moves the robot back to its initial home position. |
| `robot_programs/watering.urp` | Executes the watering motion when the soil is dry. |
| `lehre_code/` | Contains the frontend UI displayed in the CPEE frame. |
| `lehre_code/humidity.html` | Displays the soil moisture status, timestamp, sensor information, CPEE process states, and the manual check button. |
| `lehre_code/humidity.css` | Defines the UI layout, cards, status colors, moisture states, and responsive design. |
| `orange_pi/` | Contains the sensor-side code running on the Orange Pi. |
| `orange_pi/soil_sensor.py` | A lightweight Bottle-based REST API that reads the soil moisture sensor connected to GPIO pin `PH2` and returns the current moisture state as JSON. |
| `media/` | Contains static media assets used in the project. |
| `media/dry.png` | Image used to represent dry soil. |
| `media/wet.png` | Image used to represent wet soil. |

### Sensor API

The Orange Pi exposes a lightweight REST API on port `18080`. It is accessed by the CPEE workflow and the web UI to retrieve the current soil moisture state.

Example response:

```json
{
  "success": true,
  "sensor_pin": "PH2",
  "raw_state": 1,
  "soil_status": "dry",
  "timestamp": 1710000000
}
```

In this project, the sensor values are interpreted as follows:

| `raw_state` | `soil_status` | Meaning |
|---:|---|---|
| `1` | `dry` | The soil is dry and watering may be required. |
| `0` | `wet` | The soil is wet and no watering is required. |

## UI Showcase

The user interface of this project is designed to display the current soil moisture status in a clear and intuitive way.  
The raw sensor values presents 2 states: **Dry** and **Wet**.

The UI provides the following information:

- **Current Status**: Displays whether the soil is currently dry or wet
- **Moisture Level**: Visualized with a circular indicator
- **Sensor Pin**: Shows the connected sensor pin
- **Last Updated**: Displays the latest timestamp of the received data
- **Monitoring Status**: Indicates that the system is running in live monitoring mode
- **Status Message**: Provides a short explanation of the current soil condition

### Dry State UI

This page is shown when the sensor detects a dry soil condition.  
The interface highlights the dry state and indicates that watering is needed soon.

![Dry State UI](media/dry.png)

### Wet State UI

This page is shown when the sensor detects a wet soil condition.  
The interface indicates that the soil moisture is in a healthy state and no watering is needed.

![Wet State UI](media/wet.png)

## Demo Video

The experimental demonstration video of this project is available here:  
[YouTube Video](https://youtu.be/TixHz-pkvQ8)

## Notes

This repository is for academic project use only. Unauthorized redistribution or commercial use of the project materials is not permitted.

## Author

Technical University of Munich (TUM)  
Yutong Xie  
Student ID: ge94zaj
