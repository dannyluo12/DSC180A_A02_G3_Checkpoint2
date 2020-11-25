import os 
import shutil
import bagpy
import rosbag
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

def test_func(indir, outdir):
    '''
    Part of the data pipeline to transform our raw '.bag' file into csv data
    '''
    # first create the data directory
    directory = "data"
    parent_dir = "./"
    path = os.path.join(parent_dir, directory)
    
    #remove data dir if one already exists
    if (os.path.exists(path) and os.path.isdir(path)):
        shutil.rmtree(path)

    os.mkdir(path)

    # create a convenient hierarchical structure of folders inside /data
#     directory1 = "test"
#     parent_dir = "./data/"
#     data_link=os.path.join(parent_dir, directory1)
#     os.mkdir(data_link)
    os.mkdir(outdir)
    print('data directory successfully created')

    bag_path = os.path.join(indir, 'chunk_0003.bag') # this specfici bag is for test
    b = bagreader(bag_path) #might have to change this path
#     velmsgs = b.vel_data()
#     print(velmsgs)
#     veldf = pd.read_csv(velmsgs[0])

    # Read Laser Data
    laser_data = b.laser_data()
    laser_df = pd.read_csv(laser_data[0])
    laser_df.to_csv(os.path.join(outdir,'test_laser_data.csv'))
    print('Successfully added laser data to path')
    
    # Read Velocity Data
    velocity_data = b.vel_data()
    velocity_df = pd.read_csv(velocity_data[0])
    velocity_df.to_csv(os.path.join(outdir,'test_velocity_data.csv'))
    print('Successfully added velocity data to path')
    
    # Read Standard Messages
    standard_data = b.std_data()
    standard_df = pd.read_csv(standard_data[0])
    standard_df.to_csv(os.path.join(outdir,'test_standard_data.csv'))
    print('Successfully added standard data to path')
    
    # Read Odometry Data
    odometry_data = b.odometry_data()
    odometry_df = pd.read_csv(odometry_data[0])
    odometry_df.to_csv(os.path.join(outdir,'test_odometry_data.csv'))
    print('Successfully added odometry data to path')
    
    # Read Wrench Data
    wrench_data = b.wrench_data()
    wrench_df = pd.read_csv(wrench_data[0])
    wrench_df.to_csv(os.path.join(outdir,'test_wrench_data.csv'))
    print('Successfully added wrench data to path')
    
    return 

if __name__ == '__main__':
    main()

