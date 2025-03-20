import pandas as pd
import sys
import subprocess

def load_data(file_path):
    df = pd.read_csv(file_path)
    df.to_csv("loaded_data.csv", index=False)
    print("Data loaded successfully. Saved as 'loaded_data.csv'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error")
        sys.exit(1)

    dataset_path = sys.argv[1]
    load_data(dataset_path)
    subprocess.run(["python3", "dpre.py", "loaded_data.csv"])