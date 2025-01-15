import streamlit as st
import random
import time

# Function to simulate the furnace process
def furnace_simulation(target_temp, duration):
    current_temp = random.randint(20, 40)
    logs = []
    for second in range(duration):
        if current_temp < target_temp:
            current_temp += random.uniform(0.5, 1.5)
        elif current_temp > target_temp:
            current_temp -= random.uniform(0.3, 1.0)
        logs.append((second, round(current_temp, 2)))
        time.sleep(0.1)  # Simulate real-time data collection
        st.progress((second + 1) / duration)
    return logs

# Enhanced App Layout
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌡️ Furnace Temperature Monitoring App 🌡️</h1>", unsafe_allow_html=True)
st.write("Simulate and monitor furnace temperature changes over time.")

# Input Section with Columns
col1, col2 = st.columns(2)

with col1:
    target_temp = st.number_input("🎯 Target Temperature (°C):", min_value=50, max_value=2000, value=100)

with col2:
    duration = st.number_input("⏱️ Duration (seconds):", min_value=10, max_value=300, value=30)

# Button to Start Simulation
if st.button("🚀 Start Simulation"):
    st.markdown("<h3 style='color: #FF5733;'>Simulation in Progress...</h3>", unsafe_allow_html=True)
    
    # Run Simulation
    logs = furnace_simulation(target_temp, duration)
    st.success("✅ Simulation Complete!")

    # Display Results
    st.markdown("<h3 style='color: #3498DB;'>📈 Temperature Data</h3>", unsafe_allow_html=True)
    times = [log[0] for log in logs]
    temps = [log[1] for log in logs]
    st.line_chart({"Time (s)": times, "Temperature (°C)": temps})

    # Final Report
    st.markdown(
        f"<h4 style='color: #8E44AD;'>📊 Final Temperature: {temps[-1]}°C (Target: {target_temp}°C)</h4>",
        unsafe_allow_html=True,
    )
