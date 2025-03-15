import streamlit as st

# Set page title and icon
st.set_page_config(page_title="OBD-II Diagnostic Tool", page_icon="🚗", layout="wide")


# Main Page Title
st.title("🚗 OBD-II Diagnostic Tool")

# Introduction Section
st.markdown(
    """
    ### Welcome to the OBD-II Diagnostic Tool!  
    This application helps you **monitor vehicle health, diagnose issues, and analyze real-time data**  
    using an **OBD-II adapter** (WiFi).  

    ---
    ### 🔍 Features Overview:
    - **📡 WiFi Connector:** Connect to your OBD-II adapter wirelessly.
    - **📊 Dashboard:** View real-time sensor data, engine status, and fault codes.
    - **🚀 Performance Analysis:** Monitor speed, fuel efficiency, and more.

    ---
    ### 📌 How It Works:
    1. **Connect your OBD-II adapter** via WiFi (Use the *WiFi Connector* tab).
    2. **Retrieve vehicle data** and explore live metrics in the *Dashboard*.
    3. **Analyze trouble codes** to identify and resolve issues.
    4. **Optimize vehicle performance** based on sensor data insights.

    ---
    🔧 **Supported OBD-II Interfaces:**  
    - **Vgate iCar** (WiFi, Bluetooth)  
    - **ELM327** (WiFi, Bluetooth, USB)  
    - **Other ELM327-compatible adapters**  

    ---
    🚀 **Get Started by Connecting to Your Vehicle!**  
    """
)

# Footer
st.markdown("---")
st.markdown("🔧 Developed with ❤️ using Python & Streamlit")
