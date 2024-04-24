def test_file():
    with open("output/hello.txt", "w") as outputFile:
        outputFile.write("Hello Python 🐍 in Docker 🐋")

def test_plot():
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.histplot([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3])

    plt.savefig("output/report1.png")

def test_csv():
    import numpy as np
    import pandas as pd

    x = np.linspace(-np.pi, np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    df = pd.DataFrame({
        "X": x,
        "Y1": y1,
        "Y2": y2
    })

    df.to_csv("output/points.csv")

if __name__ == "__main__":
    print("Hello Python 🐍 in Docker 🐋")

    test_file()
    test_plot()
    test_csv()

    print("🚀 Done.")

