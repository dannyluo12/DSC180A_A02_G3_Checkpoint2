# Obstacle Avoidance and Path Planning

This project aims to illustrate various methods of obstacle avoidance and path planning through simulations. ROS (Robotic Operating system) navigation stacks are utilized in which gmapping and rtabmap are implemented to travel from point A to point B. Data generated from respective simulations are contained exported via rosbag files in which further exploratory data analysis can be performed. It must be noted that ROS and Ubuntu linux OS could not be loaded onto a respective dockerfile to create simulations upon launching a docker image. Therefore, rosbags were the chosen data structure to export data as they contain all the rostopic messages and its respective data. After performing EDA, plots and visualizations of the data are generated. (still can edit before submission) 

## Running the project
* Use the command `launch.sh -i dannyluo12/dsc180a-a02-g3:v2` in order to have the necessary environment to run data processing, analysis, and visualization
* symbolic link is created between respective DSMLP /teams folder and local home directory /DSC180A_A02_stuff/replication_proj_data folder

## Building the project using `run.py`
* note... will need to add the other target descriptions in here
* Use the command `python run.py test` to run the data pipeline on a subset of the data
* Use the command `python run.py all` to run the data pipeline on the whole dataset

### Contributions:
<b>Yuxi Luo</b> A14862234 <br />
Yuxi contributed by ...

<b>Seokmin Hong</b> A14614169 <br />
Seokmin contributed by ...

<b>Jia Shi</b> A15233744 <br />
Jia contributed by ...