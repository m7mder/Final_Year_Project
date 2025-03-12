import streamlit as st
import time
import obd
from utils.obd_connector import OBDConnector 
from utils.data_processor import DataProcessor
from utils.ui_helpers import UIHelpers

# Initialize OBD-II connection
obd_conn = OBDConnector()
obd_conn.connect()

# Streamlit App Configuration
st.set_page_config(page_title="OBD-II Car Dashboard", layout="wide")

st.title("🚗 Real-Time Car Dashboard")

# Display OBD-II connection status
status = "Connected" if obd_conn.connection.is_connected() else "Disconnected"
UIHelpers.display_status(status)

# Main Dashboard Loop
while obd_conn.connection.is_connected():
    # Fetch real-time car data
    speed = obd_conn.get_data(obd.commands.SPEED)
    rpm = obd_conn.get_data(obd.commands.RPM)
    fuel_level = obd_conn.get_data(obd.commands.FUEL_LEVEL)
    oil_temp = obd_conn.get_data(obd.commands.OIL_TEMP)

    # Process data
    speed = DataProcessor.process_speed(speed)
    rpm = DataProcessor.process_rpm(rpm)
    fuel_level = DataProcessor.process_fuel_level(fuel_level)
    oil_temp = DataProcessor.process_oil_temp(oil_temp)

    # Display Car Data
    UIHelpers.display_car_data(speed, rpm, fuel_level, oil_temp)

    # Display Gauges
    col1, col2 = st.columns(2)
    with col1:
        UIHelpers.display_gauge(float(speed.split()[0]), "Speed", 0, 200, "km/h")
    with col2:
        UIHelpers.display_gauge(float(rpm.split()[0]), "RPM", 0, 8000, "RPM")

    # Refresh every 1 second
    time.sleep(1)
    st.experimental_rerun()

# Show disconnected status if OBD-II device is not connected
UIHelpers.display_status("Disconnected")
