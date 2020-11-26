import sys
import json
import os

# make sure to import library code
sys.path.insert(0, 'src')

from generate_data import clean_rosdata, clean_csvdata
from util import convert_notebook
from test import test_func,clean_csv



def main(targets):

    # make sure to load up the config files
    data_cfg = json.load(open('config/data-params.json'))
    eda_cfg = json.load(open('config/eda-params.json'))
    test_cfg = json.load(open('config/test-params.json'))
    test_clean_cfg= json.load(open('config/test-clean-cfg.json'))

    if 'data' in targets:
        csvdata=clean_csvdata(**data_cfg) #takes in all arguments from data_cfg
        # if ros is installed, clean ros data
        try:
            import rospy
            rosdata = clean_rosdata()
        except:
            rosdata=[]
        
        data=[rosdata,csvdata]

    if 'eda' in targets:
        try:
            data
        except NameError:
            pass
        # execute notebook / convert to html
        convert_notebook(**eda_cfg)
        print("Please refer to the notebooks/report.html for EDA")
        
    if 'test' in targets: # edit code portion for test to run on dummy data (test data)
        try:
            import rospy
            import bagpy
            ros_csv_data = test_func(**test_cfg)
            print('Data pipeline process of converting ".bag" file into ".csv" file completed as test function. The resulting data can be seen in the "data/test/..." path.')
        except:
            print("library rospy/bagpy not loaded successfully!")
        clean_csv(**test_clean_cfg)


if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)

