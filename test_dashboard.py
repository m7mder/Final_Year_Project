import streamlit as st
import random
import time
from ui_helpers import UIHelpers

# Streamlit App Configuration
st.set_page_config(page_title="Test Dashboard", layout="wide")

st.title("🚗 OBD-II Dashboard UI Test")

# Simulated connection status
UIHelpers.display_status("Connected (Simulation)")

# Run the test loop
while True:
    # Generate random test values
    speed = random.randint(0, 200)
    rpm = random.randint(500, 7000)
    fuel_level = random.randint(0, 100)
    oil_temp = random.randint(50, 120)

    # Display test car data
    UIHelpers.display_car_data(speed, rpm, fuel_level, oil_temp)

    # Display test gauges
    col1, col2 = st.columns(2)
    with col1:
        UIHelpers.display_gauge(speed, "Speed", 0, 200, "km/h")
    with col2:
        UIHelpers.display_gauge(rpm, "RPM", 0, 8000, "RPM")

    # Refresh every second
    time.sleep(1)
    st.experimental_rerun()
