import os 

def clean_rosdata():

    directory_ros = "ros_jpeg"
    parent_dir = "./data/"
    os.mkdir(os.path.join(parent_dir, directory))
    os.system('bash ./clean.sh')



def clean_csvdata(indir, outdir):

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
    directory2 = "temp"
    directory3 = "out"
    parent_dir = "./data/"
    
    os.mkdir(os.path.join(parent_dir, directory1))
    os.mkdir(os.path.join(parent_dir, directory2))
    os.mkdir(os.path.join(parent_dir, directory3))


    # create the symlink
    os.symlink(indir, outdir) 

    data=pd.read_csv(outdir,header=None,sep=" ")
    data=data.to_numpy()
    print("data.shape :")
    print(data.shape)
    print("Fist Datapoint :")
    # print("X, Y, Speed, D_X, D_Y:")
    print(data[0])
    return data


if __name__ == '__main__':
    main()