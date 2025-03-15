import obd
import socket

class OBDConnector:
    def __init__(self, ip, port=35000):
        """
        Initialize OBD-II WiFi connection.
        :param ip: IP address of the WiFi OBD-II adapter
        :param port: Port number for the WiFi OBD-II adapter
        """
        self.ip = ip
        self.port = port
        self.connection = None

    def connect(self):
        """
        Establish connection with the OBD-II adapter.
        """
        try:
            self.connection = obd.OBD(f"socket://{self.ip}:{self.port}",baudrate=38400,timeout=1)  # Connect to the WiFi OBD device
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
