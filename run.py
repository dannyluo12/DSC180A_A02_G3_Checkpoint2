import sys
import json
import os

# make sure to import library code
sys.path.insert(0, 'src')

from generate_data import clean_rosdata,clean_csvdata
from utils import convert_notebook


def main(targets):

    # make sure to load up the config files
    data_config = json.load(open('config/data-params.json'))
    eda_config = json.load(open('config/eda-params.json'))

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
            data = pd.read_csv(data_config['outdir'])

        generate_stats(data, **eda_config)

        # execute notebook / convert to html
        convert_notebook(**eda_config)


if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)

