import sys
import json
import os

# make sure to import library code
sys.path.insert(0, 'src')

from generate_data import clean_rosdata, clean_csvdata
from util import convert_notebook
from test import test_func, plot


def main(targets):

    # make sure to load up the config files
    data_cfg = json.load(open('config/data-params.json'))
    eda_cfg = json.load(open('config/eda-params.json'))
    test_cfg = json.load(open('config/test-params.json'))
    test_plots_cfg = json.load(open('config/test-plots-params.json'))

    if 'data' in targets:
        csvdata=clean_csvdata(**data_cfg) 
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
        
    if 'test' in targets: 
        ros_csv_data = test_func(**test_cfg)
        csv_data_plots = plot(**test_plots_cfg)
        print('Data pipeline process of converting ".bag" file into ".csv" file completed as test function. The resulting data and plots can be seen in the "data/test/..." path.')


if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)