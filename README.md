# Wireless Distance-Based Relay Control Using Raspberry Pi Pico W

## Project Overview

This project utilizes the **Raspberry Pi Pico W** and the **HC-SR04 ultrasonic sensor** to create a wireless relay control system. The system measures the distance to an object using the HC-SR04 sensor and, based on this measurement, controls a relay via Wi-Fi. The relay is toggled on or off depending on the proximity of an object.

## Features

- **Distance Measurement**: The HC-SR04 sensor measures the distance to an object.
- **Wi-Fi Communication**: The Raspberry Pi Pico W sends distance data over Wi-Fi.
- **Relay Control**: A relay is activated or deactivated based on distance thresholds.
- **Real-time Automation**: The system automates the relay control in real-time.

## Components Used

- **Raspberry Pi Pico W**: Microcontroller with built-in Wi-Fi.
- **HC-SR04 Ultrasonic Sensor**: Measures the distance of an object.
- **Relay Module**: Controls an external device based on the distance.
- **Jumper wires and Breadboard**: For wiring the components.

## Software & Libraries

- **MicroPython**: Python-based programming language for the Raspberry Pi Pico W.
- **Machine Library**: For interfacing with GPIO pins on the Pico W.
- **Network Library**: For Wi-Fi communication.

## Setup

1. Connect the **HC-SR04 ultrasonic sensor** to the Raspberry Pi Pico W:
   - VCC to 5V
   - GND to GND
   - Trig to GPIO pin (e.g., GP15)
   - Echo to GPIO pin (e.g., GP14)

2. Connect the **Relay Module**:
   - VCC to 5V
   - GND to GND
   - IN to a GPIO pin (e.g., GP13)

3. Flash the **MicroPython** firmware on the Pico W.

4. Upload the script to the Raspberry Pi Pico W to measure the distance and control the relay.

SSID:- pico
password:- pico12345

