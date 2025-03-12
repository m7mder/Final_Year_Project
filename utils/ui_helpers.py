import streamlit as st
import plotly.graph_objects as go

class UIHelpers:
    """
    Provides UI components for the Streamlit dashboard.
    """

    @staticmethod
    def display_gauge(value, label, min_val=0, max_val=100, unit=""):
        """
        Creates a circular gauge to visualize real-time data.
        :param value: Current value of the parameter
        :param label: Label for the gauge
        :param min_val: Minimum value for the gauge
        :param max_val: Maximum value for the gauge
        :param unit: Measurement unit (e.g., km/h, RPM, %)
        """
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value if isinstance(value, (int, float)) else 0,
            title={'text': label},
            gauge={'axis': {'range': [min_val, max_val]}, 'bar': {'color': "blue"}},
            number={'suffix': f" {unit}"}
        ))
        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def display_status(status):
        """
        Displays connection status with color indication.
        :param status: Connection status string
        """
        color = "green" if status == "Connected" else "red"
        st.markdown(f"<h3 style='color:{color};'>🔌 OBD-II Status: {status}</h3>", unsafe_allow_html=True)

    @staticmethod
    def display_car_data(speed, rpm, fuel_level, oil_temp):
        """
        Displays car data with formatted text.
        """
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="🚗 Speed", value=f"{speed} km/h")
            st.metric(label="⛽ Fuel Level", value=f"{fuel_level} %")
        with col2:
            st.metric(label="⚙️ RPM", value=f"{rpm} RPM")
            st.metric(label="🔥 Oil Temp", value=f"{oil_temp} °C")

# Test UI components
if __name__ == "__main__":
    st.title("OBD-II Car Dashboard")
    UIHelpers.display_status("Connected")
    UIHelpers.display_car_data(80, 3000, 50, 90)
    UIHelpers.display_gauge(80, "Speed", 0, 200, "km/h")
    UIHelpers.display_gauge(3000, "RPM", 0, 8000, "RPM")
