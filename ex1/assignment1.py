# coding=utf-8

import pandas as pd
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print("file: {}".format(__file__))
print(parent_dir)

df = pd.read_csv(parent_dir + "/course1_downloads/" + "olympics.csv", index_col=0, skiprows=1)


for col in df.columns:
    if col[:2]=='01':
         df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
# df.head()

# print(df("Totals"))
# print(df.columns)
# print(df)
# print(df[df['# Summer'] > 0])
# print(df[df['# Winter'] > 0])
# print(df.iloc[3:5])

# print(df['# Summer'].idxmax())
print(type(df['Gold'].idxmax()))
print(df['Gold'].idxmax())

def answer_one():
    return df['Gold'].idxmax()

print("answer one is: {}".format(answer_one()))