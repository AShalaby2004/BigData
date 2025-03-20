import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def visualize_data(file_path):
    df = pd.read_csv(file_path)

    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) > 0:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[numeric_columns[0]], bins=20, kde=True)
        plt.title(f"Distribution of {numeric_columns[0]}")
        plt.xlabel(numeric_columns[0])
        plt.ylabel("Frequency")
        plt.savefig("vis.png")
        print("Visualization saved as 'vis.png'.")
    else:
        print("No numeric columns found for visualization.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input file provided.")
        sys.exit(1)

    input_file = sys.argv[1]
    visualize_data(input_file)

    subprocess.run(["python3", "model.py", input_file])