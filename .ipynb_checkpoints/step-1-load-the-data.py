import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import Image
import warnings

warnings.filterwarnings('ignore')

# data
# https://www.kaggle.com/miroslavsabo/paintings?select=paintings.csv
# paintings.csv

# Create dataframe
people_file_location = 'C:\data_csv\data-votes-for-art.csv'
df_orig = pd.read_csv(people_file_location)
df_orig.head(7)

print(df_orig.head(3))

