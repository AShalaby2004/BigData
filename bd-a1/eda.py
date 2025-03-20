import pandas as pd
import sys
import subprocess

def exploratory_data_analysis(file_path):
    df = pd.read_csv(file_path)


    unique_counts = df.nunique()
    with open("eda-in-1.txt", "w") as f:
        f.write("value counts per column:\n")
        f.write(str(unique_counts) + "\n")


    stats = df.describe()
    with open("eda-in-2.txt", "w") as f:
          f.write("summary of columns:\n")
          f.write(str(stats) + "\n")


    missing_values = df.isnull().sum()
    with open("eda-in-3.txt", "w") as f:
        f.write("Missing values count  column:\n")
        f.write(str(missing_values) + "\n")

    print("EDA completed. Insights saved as 'eda-in-1.txt', 'eda-in-2.txt', 'eda-in-3.txt'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input file provided.")
        sys.exit(1)
    input_file = sys.argv[1]
    exploratory_data_analysis(input_file)

    subprocess.run(["python3", "vis.py", input_file])