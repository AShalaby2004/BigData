Team Members :
1 : Abdelrahamn Shalaby
2 : Mahmoud Osama
3 : Ahmed Khairallah
__________________________________________________________________________________________________________________________________________________________

Docker-Based Data Processing Pipeline

Project Overview :

This project is designed to automate data processing, including preprocessing, analysis, visualization, and aggregation, using Docker. The pipeline takes raw dataset files, cleans and transforms them, extracts valuable insights, creates visualizations, and applies K-Means clustering to discover patterns. The entire workflow runs within a Docker container, ensuring a consistent and repeatable data processing environment
__________________________________________________________________________________________________________________________________________________________

Project Structure :

bd-a1/
Dockerfile              Defines the container environment
dataset.csv             Input dataset file
load.py                 Loads the dataset 
dpre.py                 Cleans and preprocesses the data
eda.py                  Performs Exploratory Data Analysis (EDA)
vis.py                  Generates a visualization
model.py                Applies K-Means clustering (k=3)
final.sh                Copies results to host and stops the container and add it to local device
README.md               Documentation of the project
service-result/         Folder where results are saved (created after execution)
__________________________________________________________________________________________________________________________________________________________

Technologies Used :

1_Docker
2_Python (3.x)
3_Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, Scipy
4_Bash (for automation script)
__________________________________________________________________________________________________________________________________________________________

Commands :

1 : mkdir bd-a1
2 : cd bd-a1
3 : docker build -t bd-a1-image .
4 : docker run -it --name bd-a1-container bd-a1-image
5 : docker run -it --name bd-a1-container bd-a1-image bash
6 : cd /home/doc-bd-a1/
7 : docker start -ai bd-a1-container
8 : touch load.py dpre.py eda.py vis.py model.py final.sh
9 : nano load.py
10 : nano load.py
11 : nano dpre.py
12 : nano eda.py
13 : nano vis.py
14 : nano model.py
15 : nano final.sh 
16 : chmod +x final.sh
17 : cd "C:/Users/asus/bd-a1/"
18 : chmod +x final.sh
__________________________________________________________________________________________________________________________________________________________

How to Run the Project :

Follow these steps to set up and run the pipeline:
1 : Build the Docker Image
Open a terminal in the bd-a1/ directory and build the image:

docker build -t bd-a1-image .

2 : Run the Container
Start a container from the built image:
docker run -it --name bd-a1-container bd-a1-image bash

3 : Execute the Data Pipeline
Inside the container, run:
python3 load.py dataset.csv
This will trigger the full pipeline, generating:
    res_dpre.csv => Processed dataset
    eda-in-1.txt, eda-in-2.txt, eda-in-3.txt => EDA insights
    vis.png => Visualization
    k.txt => Cluster results

4 : Copy Results and Stop Container
After the pipeline finishes, execute the following from the host machine:
chmod +x final.sh 
thin
./final.sh
This will:
Copy the generated files to bd-a1/service-result/
Stop the Docker container
__________________________________________________________________________________________________________________________________________________________

Expected Output : 
After execution, you should see the following files in bd-a1/service-result/:
service-result/
res_dpre.csv        Cleaned dataset
eda-in-1.txt        Unique value count per column
eda-in-2.txt        Statistical summary
eda-in-3.txt        Missing values report
vis.png             Visualization plot
k.txt               Cluster sizes from K-Means
__________________________________________________________________________________________________________________________________________________________

Pushing the Docker Image to Docker Hub:
Step 1: Log in to Docker Hub => docker login
step 2: Tag the Image => docker tag bd-a1-image shalaby404/bd-a1-image:latest
step 3: Push the Image =>  docker push shalaby404/bd-a1-image:latest

Image link in Doker Hub : https://hub.docker.com/r/shalaby404/bd-a1-image
__________________________________________________________________________________________________________________________________________________________

Link Files in Github : https://github.com/AShalaby2004/BigData
