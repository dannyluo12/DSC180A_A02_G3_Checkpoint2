# DSC180A_A02_G3_Checkpoint2

- Note: this repo is for DSC180A SectionA02 Group 3 project replication (Fall 2020)

This project aims to understand obstacle avoidance and path planning. Data is generated using ROS packages in conjucntion with the Intel Realsense D435i/D455 camera.
The resulting output will yield rosbag files which will need to be transformed for exploratory data analysis. 

## Running the report
### Python Run Targets
```
python run.py
```
### Target 1: Data
```
python run.py data
```
### Target 2: Run EDA
```
python run.py eda
```

### Contributions:
<b>Yuxi Luo</b> A14862234 <br />
Yuxi contributed by creating the convert.py file that converts “.bag” files into csv files directly. Also, he wrote the EDA analysis using the processed data from the csv converted files.

<b>Seokmin Hong</b> A14614169 <br />
Seokmin contributed by using the bag2csv.py file to convert the “.bag” files into csv files in order to extract useful data for the project. Also, he created the EDA graphs using the extracted information using matplotlib and pandas.

<b>Jia Shi</b> A15233744 <br />
Jia contributed by researching different ways to convert the “.bag” files created from the Realsense D435i/D455 camera into images or csv files. He also implemented the structure for the coding portion of the GitHub repo.