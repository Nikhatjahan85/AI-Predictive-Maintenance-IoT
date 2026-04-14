import pandas as pd
import time
from src.predict import predict_failure


def run_simulation():

    print("\nStarting Virtual IoT Simulation...\n")

    # Load dataset (acts like IoT sensors)
    try:
        df = pd.read_csv("data/iot_sensor_data.csv")
    except FileNotFoundError:
        print(" Dataset not found. Please check file path.")
        return

    # Loop through dataset row by row (simulate real-time data)
    for index, row in df.iterrows():

        # Extract sensor values
        temp = row.get('temperature', 0)
        vib = row.get('vibration', 0)
        curr = row.get('current', 0)

        print("--------------------------------------------------")
        print(f" Sensor Reading #{index + 1}")
        print(f" Temperature : {temp} °C")
        print(f" Vibration  : {vib}")
        print(f" Current     : {curr} A")

        # AI Prediction
        try:
            result = predict_failure(temp, vib, curr)
        except Exception as e:
            print(" Prediction error:", e)
            continue

        print("Prediction:", result)

        # Alert System
        if "Failure" in result:
            print(" ALERT: Machine Failure Detected!")
        else:
            print("Status: Machine Running Normally")

        # Save logs (important for GitHub proof)
        with open("outputs/logs.txt", "a",encoding="utf-8") as file:
            file.write(
                f"Reading {index + 1}: Temp={temp}, Vib={vib}, Curr={curr} : {result}\n"
            )

        # Delay (simulate real-time streaming)
        time.sleep(2)

    print("\n Simulation Completed!\n")