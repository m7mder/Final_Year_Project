from obd_connector import OBDConnector
import obd

# Initialize OBD Connector
obd_conn = OBDConnector(ip="192.168.0.10")
obd_conn.connect()

# Check Connection Status
if obd_conn.connection.is_connected():
    print("✅ OBD-II Bluetooth Device Connected Successfully!")
else:
    print("❌ Failed to Connect to OBD-II Device. Check Bluetooth Pairing.")
    exit()

# Test Commands
test_commands = {
    "Speed": obd.commands.SPEED,
    "RPM": obd.commands.RPM,
    "Fuel Level": obd.commands.FUEL_LEVEL,
    "Oil Temperature": obd.commands.OIL_TEMP
}

print("\n🔍 Fetching Test Data from Car ECU...\n")

for label, command in test_commands.items():
    value = obd_conn.get_data(command)
    print(f"{label}: {value}")

# Close the connection after testing
obd_conn.disconnect()
print("\n🔌 OBD-II Connection Closed.")
