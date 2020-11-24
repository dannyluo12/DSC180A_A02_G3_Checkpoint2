import os 
import pandas as pd


def clean_rosdata():
    '''
    No input. Call this function to clean the ros data
    '''
    directory_ros = "ros_jpeg"
    parent_dir = "./data/"
    os.mkdir(os.path.join(parent_dir, directory))
    os.system('bash ./src/clean.sh')


def clean_csvdata(indir_velocity, indir_odometry, indir_standard, indir_wrench, outdir_velocity, outdir_odometry, outdir_standard, outdir_wrench):

    '''
    Reads the data by creating a symlink between the 
    location of the downloaded data and /data
    '''
    # first create the data directory
    directory = "data"
    parent_dir = "./"
    path = os.path.join(parent_dir, directory)

    os.mkdir(path)

    # create a convenient hierarchical structure of folders inside /data
    directory1 = "raw"
    parent_dir = "./data/"
    data_link=os.path.join(parent_dir, directory1)
    os.mkdir(data_link)


    # create the symlink
#     os.symlink(data_link, indir)
    os.symlink(indir_velocity, outdir_velocity)
    os.symlink(indir_odometry, outdir_odometry)
    os.symlink(indir_standard, outdir_standard)
    os.symlink(indir_wrench, outdir_wrench)

#     data=pd.read_csv(data_link[csv_name],header=None,sep=" ")
#     data=data.to_numpy()
#     print("data.shape :")
#     print(data.shape)
#     print("Fist Datapoint :")
#     # print("X, Y, Speed, D_X, D_Y:")
#     print(data[0])
#     return data
    return 


if __name__ == '__main__':
    main()