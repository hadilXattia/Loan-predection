import socket

def find_available_port(start_port=5000, end_port=6000):
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                continue
    return None

available_port = find_available_port()
if available_port:
    print(f"Available port: {available_port}")
else:
    print("No available port found in the range.")
