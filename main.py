import src.visualize as viz
from src.preprocess import load_data, clean_data
from src.train import train_model

# Load data
df = load_data("data/iot_sensor_data.csv")

# Clean
df = clean_data(df)

# Train
model = train_model(df)



# plot graph
viz.plot_data(df)

# run simulation
from src.simulator import run_simulation
run_simulation()


from src.predict import predict_failure

result = predict_failure(70, 30, 10)
print("Prediction:", result)