import network
import time
import urequests
from machine import Pin, time_pulse_us

# Relay Pico W AP credentials
SSID = "pico"
PASSWORD = "pico12345"
RELAY_PICO_IP = "192.168.4.1"
RELAY_URL = f"http://{RELAY_PICO_IP}/update?state="

# HC-SR04 Pins
TRIG = Pin(2, Pin.OUT)
ECHO = Pin(3, Pin.IN)

# Connect to Relay Pico AP
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(SSID, PASSWORD)

print("Connecting to Relay Pico W...")
while not sta.isconnected():
    time.sleep(0.5)

print(f"✅ Connected to Relay Pico W at IP: {RELAY_PICO_IP}")
print("Sensor is active and sending commands based on distance...")

# Function to measure distance
def measure_distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

    try:
        pulse = time_pulse_us(ECHO, 1, 30000)  # Timeout 30ms
        dist_cm = (pulse / 2) / 29.1
        return round(dist_cm, 2)
    except:
        return None

last_state = None

# Main loop
while True:
    distance = measure_distance()
    if distance is not None:
        print("Distance:", distance, "cm")
        try:
            if distance < 10 and last_state != "on":
                r = urequests.get(RELAY_URL + "on")
                print("🔁 Sent ON command:", r.text)
                r.close()
                last_state = "on"
            elif distance >= 10 and last_state != "off":
                r = urequests.get(RELAY_URL + "off")
                print("🔁 Sent OFF command:", r.text)w
                r.close()
                last_state = "off"
        except Exception as e:
            print(" contact Relay Pico:", e)
    else:
        print("⚠️ Measurement failed or out of range")

    time.sleep(2)

