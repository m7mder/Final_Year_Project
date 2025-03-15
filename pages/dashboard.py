import streamlit as st
import obd
import time
from obd_connector import OBDConnector

# Set up the Streamlit page
st.set_page_config(page_title="OBD-II Dashboard", page_icon="📊", layout="wide")

# Sidebar title
st.sidebar.title("Dashboard")

# Input fields for OBD-II connection
st.sidebar.subheader("🔌 Connect to OBD-II")
ip_address="192.168.0.10"


# Connect Button
if st.sidebar.button("Connect"):
    obd_conn = OBDConnector(ip=ip_address)
    obd_conn.connect()
    st.session_state["obd_conn"] = obd_conn  # Store connection in session

# Check if connection exists
if "obd_conn" in st.session_state:
    obd_conn = st.session_state["obd_conn"]
    if obd_conn.connection and obd_conn.connection.is_connected():
        st.sidebar.success("✅ Connected to OBD-II!")

        # Layout for displaying vehicle data
        col1, col2, col3 = st.columns(3)

        # Fetch OBD-II data
        rpm = obd_conn.get_data(obd.commands.RPM)
        throttle_pos = obd_conn.get_data(obd.commands.THROTTLE_POS)
        speed = obd_conn.get_data(obd.commands.SPEED)
        coolant_temp = obd_conn.get_data(obd.commands.COOLANT_TEMP)
        bar_pressure = obd_conn.get_data(obd.commands.BAROMETRIC_PRESSURE)
        voltage = obd_conn.get_data(obd.commands.ELM_VOLTAGE)

        # Extract values from STATUS command
        status_response = obd_conn.connection.query(obd.commands.STATUS)
        if status_response.value:
            status_dict = status_response.value.__dict__  # Convert to dictionary
        else:
            status_dict = {}

        # Display Data
        with col1:
            st.metric(label="🚗 RPM", value=rpm)
            st.metric(label="⚡ Voltage", value=voltage)
        with col2:
            st.metric(label="🏎️ Speed (km/h)", value=speed)
            st.metric(label="🌡️ Coolant Temp (°C)", value=coolant_temp)
        with col3:
            st.metric(label="🔧 Throttle Position (%)", value=throttle_pos)
            st.metric(label="🌬️ Barometric Pressure (kPa)", value=bar_pressure)

        # Status Information
        st.subheader("🔍 Vehicle Status")
        st.json(status_dict)  # Display extracted status info in JSON format

    else:
        st.sidebar.error("❌ Connection Failed! Please check the IP & Port.")

# Footer
st.markdown("---")
st.markdown("🚗 Developed with ❤️ using Python & Streamlit")
