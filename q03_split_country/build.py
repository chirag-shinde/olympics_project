# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    'write your solution here'
    df = q02_rename_columns(path)
    country_name = df['country name'].str.split().apply(lambda x: x[0])
    df.rename(index=country_name,inplace=True)
    df.drop(['country name'], axis=1,inplace=True)
    return df[:-1]
q03_summer_gold_medals('./data/olympics.csv')

