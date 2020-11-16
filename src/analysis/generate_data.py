import os
import bagpy
import rosbag
import pandas as pd
import seaborn as sea
import numpy as np
from bagpy import bagreader
from matplotlib import pyplot as plt

#reading the bag
b = bagreader('example.bag')
# b.topic_table

#decoding messages by the topics


velmsgs   = b.vel_data()
veldf = pd.read_csv(velmsgs[0])

veldf.to_csv('bag_data_csv')


# visualizations
# fig = bagpy.animate_timeseries(veldf['Time'], veldf['linear.x'], title='Velocity Timeseries')
# fig.savefig('ex_img.png')
# plt.close(fig)

######################################################################################################

# def clean_rosdata():
#     os.system('bash ./clean.sh')
#
#
# 
# def clean_csvdata(json_file, key):
#     data=pd.read_csv(json_file[key],header=None,sep=" ")
#     data=data.to_numpy()
#     print("data.shape :")
#     print(data.shape)
#     print("Fist Datapoint :")
#     # print("X, Y, Speed, D_X, D_Y:")
#     print(data[0])
######################################################################################################


if __name__ == '__main__':
    main()
