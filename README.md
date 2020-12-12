# Obstacle Avoidance and Path Planning

This project aims to illustrate various methods of obstacle avoidance and path planning through simulations. ROS (Robotic Operating system) navigation stacks are utilized in which gmapping and rtabmap are implemented to travel from point A to point B. Data generated from respective simulations are contained exported via rosbag files in which further exploratory data analysis can be performed. It must be noted that ROS and Ubuntu linux OS could not be loaded onto a respective dockerfile to create simulations upon launching a docker image. Therefore, rosbags were the chosen data structure to export data as they contain all the rostopic messages and its respective data. After performing EDA, plots and visualizations of the data are generated. (still can edit before submission) 

## Running the project
* Use the command `launch.sh -i elvishelvis/dsc180s2g3 -c 4 -m 8  -P Always` in order to have the necessary environment to run data processing, analysis, and visualization

## Building the project using `run.py`
* Use the commang `python run.py data` to create the data folder. Created via a symbolic link to our data directory in the /teams directory (accessible only if you are on UC San Diego DSMLP server)
* Use the command `python run.py test` to run the data pipeline on a subset of the data
* Use the command `python run.py all` to run the data pipeline on the whole dataset

### Contributions:
<b>Yuxi Luo</b> A14862234 <br />
Yuxi contributed by ...

<b>Seokmin Hong</b> A14614169 <br />
Seokmin contributed by ...

<b>Jia Shi</b> A15233744 <br />
Jia contributed by ...