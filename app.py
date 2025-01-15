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

# Button to Start Simulation
if st.button("🚀 Start Simulation"):
    st.markdown("<h3 style='color: #FF5733;'>Simulation in Progress...</h3>", unsafe_allow_html=True)
    
    # Add a single progress bar object
    progress_bar = st.progress(0)

    # Run Simulation
    logs = furnace_simulation(target_temp, duration)

    # Update Progress Bar
    for i in range(len(logs)):
        progress_bar.progress((i + 1) / len(logs))

    st.success("✅ Simulation Complete!")

    # Extract data
    times = [log[0] for log in logs]
    temps = [log[1] for log in logs]

    # Identify steady-state time
    threshold = 1.0  # ±1°C tolerance
    steady_state_time = next((t for t, temp in logs if abs(temp - target_temp) <= threshold), None)

    # Plot Results
    st.markdown("<h3 style='color: #3498DB;'>📈 Temperature vs Time</h3>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, color='blue', label='Temperature')
    plt.axhline(y=target_temp, color='red', linestyle='--', label='Target Temperature')
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Furnace Temperature Monitoring")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

    # Display Final Report
    st.markdown(f"<h4 style='color: #8E44AD;'>📊 Final Temperature: {temps[-1]}°C (Target: {target_temp}°C)</h4>", unsafe_allow_html=True)
    if steady_state_time is not None:
        st.markdown(
            f"<h4 style='color: #2ECC71;'>⏱️ Steady-State Achieved at: {steady_state_time} seconds</h4>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<h4 style='color: #E74C3C;'>⚠️ Steady-State Not Achieved During Simulation</h4>",
            unsafe_allow_html=True,
        )
