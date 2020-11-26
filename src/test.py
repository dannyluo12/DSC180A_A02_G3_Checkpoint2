import os 
import shutil
import bagpy
import rosbag
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import os.path as osp

def test_func(indir, outdir):
    '''
    Part of the data pipeline to transform our raw '.bag' file into csv data for further EDA (exploratory data analysis)
    
    note: was able to utilize bagpy and rosbag on the ucsdets/scipy-ml-notebook docker image
    '''
    # first create the data directory
    directory = "data"
    parent_dir = "./"
    path = os.path.join(parent_dir, directory)
    
    #remove data dir if one already exists
    if (os.path.exists(path) and os.path.isdir(path)):
        shutil.rmtree(path)

    os.mkdir(path)
    os.mkdir(outdir)
    print('data directory successfully created')

    bag_path = os.path.join(indir, 'test_0006.bag') # this specfici bag is for test
    b = bagreader(bag_path) #might have to change this path
#     velmsgs = b.vel_data()
#     print(velmsgs)
#     veldf = pd.read_csv(velmsgs[0])

    # Read Laser Data
    laser_data = b.laser_data()
    laser_df = pd.read_csv(laser_data[0])
    laser_df.to_csv(os.path.join(outdir,'test_laser_data.csv'))
    print('Successfully added laser data from .bag file to path')
    
    # Read Velocity Data
    velocity_data = b.vel_data()
    velocity_df = pd.read_csv(velocity_data[0])
    velocity_df.to_csv(os.path.join(outdir,'test_velocity_data.csv'))
    print('Successfully added velocity data from .bag file to path')
    
    # Read Standard Messages
    standard_data = b.std_data()
    standard_df = pd.read_csv(standard_data[0])
    standard_df.to_csv(os.path.join(outdir,'test_standard_data.csv'))
    print('Successfully added standard data from .bag file to path')
    
    # Read Odometry Data
    odometry_data = b.odometry_data()
    odometry_df = pd.read_csv(odometry_data[0])
    odometry_df.to_csv(os.path.join(outdir,'test_odometry_data.csv'))
    print('Successfully added odometry data from .bag file to path')
    
    # Read Wrench Data
    wrench_data = b.wrench_data()
    wrench_df = pd.read_csv(wrench_data[0])
    wrench_df.to_csv(os.path.join(outdir,'test_wrench_data.csv'))
    print('Successfully added wrench data from .bag file to path')
    
    return 
def clean_csv(odom_data, standard_data, velocity_data, outdir):
    '''
    function to save clean csv to outdirectory: "./data/test/clean"
    '''
    os.mkdir(outdir) # should create "./data/test/clean" folder path because data folder already created in func above
    velocity_df = pd.read_csv(velocity_data)
    odometry_df = pd.read_csv(odom_data)
    standard_df = pd.read_csv(odom_data)
    
    velocity_cleaned = velocity_df.drop(["Unnamed: 0"], axis=1)
    odometry_cleaned = odometry_df.drop(["Unnamed: 0"], axis=1)
    standard_cleaned = standard_df.drop(["Unnamed: 0"], axis=1)
    print('CSV data successfully cleaned')

    velocity_name=osp.join(outdir,velocity_data.split('/')[-1])
    standard_name=osp.join(outdir,standard_data.split('/')[-1])
    odom_name=osp.join(outdir,odom_data.split('/')[-1])

    velocity_cleaned.to_csv(velocity_name)
    odometry_cleaned.to_csv(standard_name)
    standard_cleaned.to_csv(odom_name)
    print('cleaned CSV successfully save to path "./data/test/clean"')
if __name__ == '__main__':
    main()

