# %load q02_rename_columns/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

def q02_rename_columns(path):
    'write your solution here'
    df = q01_load_data(path)
    df = df.rename(columns={'01 !':'Gold', '02 !':'Silver', '03 !':'Bronze'})
    return df

print(type(q02_rename_columns('./data/olympics.csv')))

