import streamlit as st
import subprocess

def get_wifi_networks():
    """Scans for available Wi-Fi networks and returns a list."""
    try:
        result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True)
        lines = result.stdout.split("\n")
        networks = [line.split(":")[1].strip() for line in lines if "SSID" in line]
        return networks
    except Exception as e:
        return [f"Error: {str(e)}"]

# Streamlit UI
st.title("Wi-Fi Selector")

wifi_list = get_wifi_networks()

if wifi_list:
    selected_wifi = st.selectbox("Select a Wi-Fi Network:", wifi_list)

    if st.button("Connect"):
        st.write(f"Selected Wi-Fi: **{selected_wifi}**")
        # You can add code to connect using subprocess here
else:
    st.error("No Wi-Fi networks found.")
