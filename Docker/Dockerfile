# 1) choose base container
# generally use the most recent tag

# data science notebook
# https://hub.docker.com/repository/docker/ucsdets/datascience-notebook/tags
ARG BASE_CONTAINER=ros:melodic

# scipy/machine learning (tensorflow)
# https://hub.docker.com/repository/docker/ucsdets/scipy-ml-notebook/tags
# ARG BASE_CONTAINER=ucsdets/scipy-ml-notebook:2020.2-stable

FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

# 2) change to root to install packages
USER root

RUN apt-get update
RUN apt-get -y install jupyter-notebook
RUN apt-get -y install vim
# 3) install packages
# RUN pip install --no-cache-dir networkx scipy python-louvain

# 4) change back to notebook user
COPY /run_jupyter.sh /
RUN chmod 777 /run_jupyter.sh

# RUN ["/bin/bash", "-c", "set -e"]
# RUN ["/bin/bash", "-c", "source /opt/ros/$ROS_DISTRO/setup.bash"]
# RUN exec "$@"



USER $NB_UID

ENTRYPOINT set -e && source /opt/ros/$ROS_DISTRO/setup.bash && exec "$@" && /bin/bash

# Override command to disable running jupyter notebook at launch
# CMD ["/bin/bash"]

