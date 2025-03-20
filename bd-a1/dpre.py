import pandas as pd
import sys
import subprocess

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    df.to_csv("res_dpre.csv", index=False)
    print("Data cleaned successfully. Saved as 'res_dpre.csv'.")

if __name__ == "__main__":
     if len(sys.argv) < 2:
        print("Error: No input file provided.")
        sys.exit(1)

     input_file = sys.argv[1]
     clean_data(input_file)

     subprocess.run(["python3", "eda.py", "res_dpre.csv"])