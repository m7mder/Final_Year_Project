class DataProcessor:
    """
    Processes raw OBD-II data before displaying on the dashboard.
    """

    @staticmethod
    def process_speed(speed):
        """
        Converts speed from km/h to mph if needed.
        :param speed: Speed in km/h
        :return: Processed speed in km/h (default) or mph
        """
        if speed == "N/A":
            return "No Data"
        try:
            speed_kmh = float(speed.magnitude)  # Extracts numerical value
            return f"{speed_kmh:.1f} km/h"
        except Exception:
            return "Invalid Data"

    @staticmethod
    def process_rpm(rpm):
        """
        Validates RPM value.
        :param rpm: RPM value
        :return: Processed RPM string
        """
        if rpm == "N/A":
            return "No Data"
        try:
            rpm_value = int(rpm.magnitude)
            return f"{rpm_value} RPM" if rpm_value >= 0 else "Invalid RPM"
        except Exception:
            return "Invalid Data"

    @staticmethod
    def process_fuel_level(fuel_level):
        """
        Ensures fuel level is within valid range (0-100%).
        :param fuel_level: Fuel level percentage
        :return: Processed fuel level string
        """
        if fuel_level == "N/A":
            return "No Data"
        try:
            fuel = float(fuel_level.magnitude)
            if 0 <= fuel <= 100:
                return f"{fuel:.1f}%"
            return "Invalid Fuel Level"
        except Exception:
            return "Invalid Data"

    @staticmethod
    def process_oil_temp(oil_temp):
        """
        Converts oil temperature to Celsius.
        :param oil_temp: Oil temperature in °C
        :return: Processed oil temperature string
        """
        if oil_temp == "N/A":
            return "No Data"
        try:
            temp_c = float(oil_temp.magnitude)
            return f"{temp_c:.1f}°C"
        except Exception:
            return "Invalid Data"

# Test processing functions
if __name__ == "__main__":
    test_data = {
        "speed": 80,       # km/h
        "rpm": 3000,       # RPM
        "fuel_level": 50,  # %
        "oil_temp": 90     # °C
    }

    processor = DataProcessor()
    print(f"🚗 Speed: {processor.process_speed(test_data['speed'])}")
    print(f"⚙️ RPM: {processor.process_rpm(test_data['rpm'])}")
    print(f"⛽ Fuel Level: {processor.process_fuel_level(test_data['fuel_level'])}")
    print(f"🔥 Oil Temp: {processor.process_oil_temp(test_data['oil_temp'])}")
