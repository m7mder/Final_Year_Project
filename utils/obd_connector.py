import obd

class OBDConnector:
    def __init__(self, port=None, baudrate=9600):
        """
        Initialize OBD-II Bluetooth connection.
        :param port: Bluetooth serial port (e.g., "/dev/rfcomm0" on Linux, "COM5" on Windows)
        :param baudrate: Default baud rate for ELM327 devices
        """
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        """
        Establish connection with the OBD-II adapter.
        """
        try:
            self.connection = obd.OBD()  # Auto-connect to the first available Bluetooth OBD device
            if self.connection.is_connected():
                print("✅ Connected to OBD-II device successfully!")
            else:
                print("❌ Failed to connect to OBD-II device.")
        except Exception as e:
            print(f"⚠️ Connection Error: {e}")

    def get_data(self, pid):
        """
        Fetch live data for a given OBD-II parameter.
        :param pid: OBD-II command (e.g., obd.commands.RPM, obd.commands.SPEED)
        :return: Parsed sensor value
        """
        if self.connection and self.connection.is_connected():
            response = self.connection.query(pid)
            return response.value if response.value is not None else "N/A"
        return "Disconnected"

    def disconnect(self):
        """
        Close the OBD-II connection.
        """
        if self.connection:
            self.connection.close()
            print("🔌 Disconnected from OBD-II device.")

# Test the connection
if __name__ == "__main__":
    obd_conn = OBDConnector()
    obd_conn.connect()
    
    print(f"🚗 Speed: {obd_conn.get_data(obd.commands.SPEED)}")
    print(f"⚙️ RPM: {obd_conn.get_data(obd.commands.RPM)}")
    print(f"⛽ Fuel Level: {obd_conn.get_data(obd.commands.FUEL_LEVEL)}")
    print(f"🔥 Oil Temp: {obd_conn.get_data(obd.commands.OIL_TEMP)}")

    obd_conn.disconnect()
