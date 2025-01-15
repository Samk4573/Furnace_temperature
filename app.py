import streamlit as st
import random
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
    return logs

# Plot the simulation data
def plot_furnace_data(logs, target_temp):
    times = [log[0] for log in logs]
    temps = [log[1] for log in logs]
    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, label="Current Temperature")
    plt.axhline(y=target_temp, color="red", linestyle="--", label="Target Temperature")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Furnace Temperature Monitoring")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Streamlit App Layout
st.title("Furnace Temperature Monitoring App")

# Inputs
target_temp = st.number_input("Enter Target Temperature (°C):", min_value=50, max_value=2000, value=100)
duration = st.number_input("Enter Duration (seconds):", min_value=10, max_value=300, value=30)

# Run Simulation
if st.button("Start Simulation"):
    logs = furnace_simulation(target_temp, duration)
    st.write(f"Simulation completed for target temperature: {target_temp}°C and duration: {duration} seconds.")
    plot_furnace_data(logs, target_temp)
