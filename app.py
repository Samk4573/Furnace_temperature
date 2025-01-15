import streamlit as st
import random
import time
import matplotlib.pyplot as plt

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
    
    # Add a single progress bar object
    progress_bar = st.progress(0)

    # Run Simulation
    logs = []
    current_temp = random.randint(20, 40)

    for second in range(duration):
        if current_temp < target_temp:
            current_temp += random.uniform(0.5, 1.5)
        elif current_temp > target_temp:
            current_temp -= random.uniform(0.3, 1.0)
        logs.append((second, round(current_temp, 2)))

        # Update progress bar
        progress_bar.progress((second + 1) / duration)
        time.sleep(0.1)  # Simulate real-time data collection

    st.success("✅ Simulation Complete!")

    # Display Results
    st.markdown("<h3 style='color: #3498DB;'>📈 Temperature vs Time</h3>", unsafe_allow_html=True)

    # Extract data
    times = [log[0] for log in logs]
    temps = [log[1] for log in logs]

    # Plot with Matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, marker='o', color='blue', label='Temperature')
    plt.axhline(y=target_temp, color='red', linestyle='--', label='Target Temperature')
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Furnace Temperature Monitoring")
    plt.legend()
    plt.grid(True)
    
    # Render the plot
    st.pyplot(plt)

    # Final Report
    st.markdown(
        f"<h4 style='color: #8E44AD;'>📊 Final Temperature: {temps[-1]}°C (Target: {target_temp}°C)</h4>",
        unsafe_allow_html=True,
    )
