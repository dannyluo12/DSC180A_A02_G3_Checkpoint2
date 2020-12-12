import sys
import json
import os

sys.path.insert(0, 'src')

from etl import get_data
from util import convert_notebook
from test import test_func, plot


def main(targets):

    # make sure to load up the config files
    data_cfg = json.load(open('config/data-params.json'))
    eda_cfg = json.load(open('config/eda-params.json'))
    test_cfg = json.load(open('config/test-params.json'))
    test_plots_cfg = json.load(open('config/test-plots-params.json'))
        
    if 'data' in targets:
        getting_data = get_data(**data_cfg)
        print('Data from project successfully pulled intp /data/raw folder.')
        
    if 'test' in targets: 
        ros_csv_data = test_func(**test_cfg)
        csv_data_plots = plot(**test_plots_cfg)
        print('Data pipeline process of converting ".bag" file into ".csv" file completed as test function. The resulting data and plots can be seen in the "data/test/..." path.')
        
    if 'all' in targets:
        ros_csv_data = test_func(**test_cfg)
        csv_data_plots = plot(**test_plots_cfg)
        print('Data pipeline process of converting ".bag" file into ".csv" file completed as test function. The resulting data and plots can be seen in the "data/test/..." path.')


if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)