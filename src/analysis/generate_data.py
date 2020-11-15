import os 

def clean_rosdata():
    os.system('bash ./clean.sh')



def clean_csvdata(json_file, key):
    data=pd.read_csv(json_file[key],header=None,sep=" ")
    data=data.to_numpy()
    print("data.shape :")
    print(data.shape)
    print("Fist Datapoint :")
    # print("X, Y, Speed, D_X, D_Y:")
    print(data[0])


if __name__ == '__main__':
    main()