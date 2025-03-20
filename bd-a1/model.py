import pandas as pd
from sklearn.cluster import KMeans
import sys

def apply_kmeans(file_path, k=3):
    df = pd.read_csv(file_path)

    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.shape[1] == 0:
        print("No numeric columns available for clustering.")
        return


    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(numeric_df)
    df['Cluster'] = clusters

    cluster_counts = df['Cluster'].value_counts().sort_index()

    with open("k.txt", "w") as f:
        f.write("Cluster counts:\n")
        f.write(str(cluster_counts) + "\n")

    print("K-means clustering completed. Results saved in 'k.txt'.") 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input.")
        sys.exit(1)

    input_file = sys.argv[1]
    apply_kmeans(input_file)