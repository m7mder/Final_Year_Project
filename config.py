import serial.tools.list_ports

def find_obd_port():
    """
    Automatically detects the OBD-II Bluetooth COM port on Windows.
    :return: COM port string (e.g., 'COM5') or None if not found
    """
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "OBD" in port.description or "ELM327" in port.description:
            return port.device  # Returns something like 'COM5'
    return None  # No valid OBD-II device found

CONFIG = {
    "BLUETOOTH_PORT": find_obd_port() or "COM5",  # Auto-detect, fallback to COM5
    "BAUD_RATE": 9600,         # Standard baud rate for ELM327
    "TIMEOUT": 2,              # Timeout for OBD-II responses
    "DEBUG": True              # Enable debugging messages
}

if CONFIG["DEBUG"]:
    print(f"🔍 Auto-Detected OBD-II Port: {CONFIG['BLUETOOTH_PORT']}")
