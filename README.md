# DSC180A_A02 Group 3 (Methodology 7)

- Note: This specific branch (methodology_7) is used to showcase current work as well as demonstrating the test target.

This project aims to understand obstacle avoidance and path planning. Data is generated using ROS packages in conjucntion with the Intel Realsense D435i/D455 camera.
The resulting output will yield rosbag files which will need to be transformed for exploratory data analysis. Transforming the data generated from the camera is part of the data pipeline process. In this methodology, I will demonstrate this transformation of data from ".bag" data into ".csv" data. 

### Most of the coding materials of our project is based on ROS Gazebo and Donkey AI simulation, thus most of our core code are in local computer rather than to be included in this repo.

## Running the report
```
python run.py data
```
### and 
```
python run.py all
```
Make sure to run 'data' target before run 'all' target
## Python Run Target (test)
```
python run.py test
```

## Contribution

### Jia Shi A15233744

Conducted comparison study for different navigation algorithm with Donkey AI. Built up the docker-file and the real time model prediction visualization Donkey car. Research on the evaluation metrics as well as the efficiency of applying different navigation algorithms into different situation. Contributed to the weekly discussion and helped to organize the GitHub-repo, checkpoint and reports. Contributed to the development of ROS navigation on path planing and obstacle avoidance. 
