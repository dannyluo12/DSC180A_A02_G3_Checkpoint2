
'''
This script utilizes the bagpy library to open and dissect ".bag" files into other data types such as ".csv".  We use
this script to seperate our bag gile into specific types of data (i.e laser data, velocity data, odometry data, etc.)
based on different bag reader tags. We then use the different data types to perform EDA.
'''


from bagpy import bagreader
import bagpy
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
b = bagreader('/home/ucsd/bagpy/origin.bag')

# Read Laser Data
laser_data = b.laser_data()
laser_df = pd.read_csv(laser_data[0])
laser_df.to_csv('laser_data.csv')

# Read Velocity Data
velocity_data = b.vel_data()
velocity_df = pd.read_csv(velocity_data[0])
velocity_df.to_csv('velocity_data.csv')

# Read Standard Messages
standard_data = b.std_data()
standard_df = pd.read_csv(standard_data[0])
standard_df.to_csv('standard_data.csv')

# Read Odometry Data
odometry_data = b.odometry_data()
odometry_df = pd.read_csv(odometry_data[0])
odometry_df.to_csv('odometry_data.csv')

# Read Wrench Data
wrench_data = b.wrench_data()
wrench_df = pd.read_csv(wrench_data[0])
wrench_df.to_csv('wrench_data.csv')

# from bagpy import bagreader
# import bagpy
# import pandas as pd
# import seaborn as sea
# import matplotlib.pyplot as plt
# b = bagreader('/home/ucsd/bagpy/origin.bag')
#
#
# # Read Velocity Data
# ms = b.vel_data()
# vel = pd.read_csv(ms[0])
#
# # Read Standard Messages
# s = b.std_data()
# data = pd.read_csv(s[0])
#
# # Read odometry Data
# odom = b.odometry_data()
# odomdata = pd.read_csv(odom[0])
#
# # Read Wrench Data
# w = b.wrench_data()
# wdata = pd.read_csv(w[0])
#
# # Get the plots
# #b.plot_odometry()
# #b.plot_vel()
# #b.plot_wrench()

############################################################################

# import bagpy
# import rosbag
# import pandas as pd
# from bagpy import bagreader
#
# b = bagreader('/home/ucsd/bagpy/origin.bag')
# velmsgs   = b.vel_data()
# veldf = pd.read_csv(velmsgs[0])
#
# veldf.to_csv('bag_data_csv')
# bagpy.animate_timeseries(veldf['Time'], veldf['linear.x'], title='Velocity Timeseries')
#
