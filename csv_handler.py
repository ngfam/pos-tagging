import csv
import pandas as pd

a = pd.read_csv('Datas/train.csv')
b = pd.read_csv('Datas/tags.csv')
merged = a.merge(b, how = 'left', on = ['sentence_id', 'token_id'])
merged = merged[['sentence_id', 'before', 'after', 'pos']]

merged.to_csv('Datas/pos_training.csv')