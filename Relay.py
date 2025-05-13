import network
import socket
import time
from machine import Pin

# Access Point Credentials
SSID = "pico"
PASSWORD = "pico12345"

# Set up AP Mode
ap = network.WLAN(network.AP_IF)
ap.active(True)
time.sleep(1)
ap.config(essid=SSID, password=PASSWORD)

while not ap.active():
    pass

# Display network info
ip_address = ap.ifconfig()[0]
print("Access Point is active.")
print(f"Relay Pico W IP Address: {ip_address}")
print("Server is running and waiting for connections...")

# Setup Relay on GPIO15
relay = Pin(15, Pin.OUT)
relay.off()

# Web Server Function
def web_server():
    addr = ("0.0.0.0", 80)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)  # 1 client at a time is enough for this setup
    print("Listening on port 80...")

    while True:
        try:
            print("Waiting for client connection...")
            conn, client_addr = s.accept()
            print("Client connected from:", client_addr)

            request = conn.recv(1024).decode()
            print("Request received:", request)

            if "GET /update?" in request:
                try:
                    query = request.split(" ")[1]
                    _, params = query.split("?")
                    key, value = params.split("=")
                    key = key.lower()
                    value = value.lower()

                    if key in ["state", "status"]:
                        if value == "on":
                            relay.value(1)
                            print("Relay turned ON")
                        elif value == "off":
                            relay.value(0)
                            print("Relay turned OFF")
                        else:
                            raise ValueError("Invalid value")

                        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nRelay updated"
                    else:
                        raise ValueError("Invalid key")

                except Exception as e:
                    print("Parsing error:", e)
                    response = "HTTP/1.1 400 Bad Request\r\n\r\nInvalid request format"

            else:
                response = "HTTP/1.1 404 Not Found\r\n\r\nNot Found"

            conn.sendall(response.encode())

        except Exception as e:
            print("Error:", e)

        finally:
            try:
                conn.close()
            except:
                pass

# Run the server
web_server()

