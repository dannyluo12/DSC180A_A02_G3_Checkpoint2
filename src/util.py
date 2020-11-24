import os

def convert_notebook(a,b):
    '''
    Should try to make this python script to somehow run the .ipynb notebook and convert into html? ASK TA
    
    # may have this error
    # xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex.
    '''
    try:
        os.system ("jupyter nbconvert --no-input --to pdf --output ./notebooks/report.pdf ./notebooks/report.ipynb")
    except:
        os.system("jupyter nbconvert --to html ./notebooks/report.ipynb  --output report")