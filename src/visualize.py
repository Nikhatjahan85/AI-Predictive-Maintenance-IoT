import matplotlib.pyplot as plt

def plot_data(df):
    plt.figure()
    plt.scatter(df['temperature'], df['failure'])
    plt.xlabel("Temperature")
    plt.ylabel("Failure")
    plt.title("Failure vs Temperature")

    plt.savefig("images/graph.png")
    plt.show()