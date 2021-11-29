#!/usr/bin/env python
# coding: utf-8

# # Here
# basic Data Analysis of Votes data for 39 Art Works rated by 48 participants with 1 to 5 score. 

# ### project
# 
# Analyzing and Preparing Data for Learning Algoritms to give user recomendations based on their previous choice
# 
# by AnnaKonda (annakonda.guru annakonda.live annakonda.co annakonda.online ) https://github.com/annakoopenu/PeoplePeoplePeople

# ### about the data
# 
# Based on db:
#  https://www.kaggle.com/miroslavsabo/paintings
#  https://www.kaggle.com/anako2020/paintings-data-exploration
#  
#  39 Art Works by famous painters 
#  Rated by 48 questionary participant's score 1 to 5

# using only 3 python's packages
# - pandas
# - numpy
# - matplotlib.pyplot 

# # Step 0 - Loading the Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import math

from IPython.display import Image
import warnings
warnings.filterwarnings('ignore')


# data
# paintings.csv

# Create dataframe  
people_file_location = 'paintings.csv'
df_orig = pd.read_csv(people_file_location)


# # Step 1 - Data First Overlook

# Overlook at the given data, it's volume, columns types and features. 
# 

df_orig.head()
df_orig['art movement'].unique().tolist()


# 48 participants rated 39 paintings of 39 different artists, 3 for each of 13 different art movements.
# For example, 'Art Nouveau' movement consists of 3 following paintings by 3 artists: Gustav Klimt, Pierre Bonnard and Alfonz Mucha.
# 

# ### (1) art piece's rating

df_rating = pd.DataFrame(df_orig)
df_rating = df_rating.set_index('artist')
df_rating = df_rating.drop(columns=['art movement','painting'])

# Statistics for votes of 48 voters
df_rating.describe().loc[['count','mean','std']]

mean_rate = round(df_rating.describe().loc['mean'].mean(), 2)
mean_rate_std = round(df_rating.describe().loc['std'].mean(), 2)
raitings = df_rating.describe().loc['mean']
raitings = np.sort(raitings)

# show histogram for Artist's rating score 
fig, ax = plt.subplots(figsize=(15,5))

ax.hist(raitings, bins = 13)
ax.set_title('Mean Rating score for  ' + str(df_rating.shape[0]) +' art pieces' + ' rated by 48 participants')
ax.set_xticks([1,2,3,4,5])

ax.axvline(mean_rate, ls='--', color='r', label=str(mean_rate))
ax.axvline(mean_rate + math.sqrt(mean_rate_std), ls='--', color='g', label=str('+std'))
ax.axvline(mean_rate - math.sqrt(mean_rate_std), ls='--', color='g', label=str('-std'))

ax.set_xlabel(str(mean_rate), color='r')

fig.show()


# ### (2) participant's scores

df_scores = pd.DataFrame(df_rating)
df_scores = df_scores.transpose()
#df_scores.head(3)

# Statistics for rates of 39 art pieces
df_scores.describe().loc[['count','mean','std']]

df_scores.describe().loc['mean'].mean()
mean_score = round(df_scores.describe().loc['mean'].mean(),2)
mean_scores_std = round(df_scores.describe().loc['std'].mean(), 2)
scores = df_scores.describe().loc['mean']
scores = np.sort(scores)

# show histogram for User's rating score 
fig, ax = plt.subplots(figsize=(15,5))

ax.hist(scores, bins = 13)
ax.set_title('Mean Rating score for  ' + str(df_scores.shape[0]) +' art pieces' + ' rated by 48 participants')
ax.set_xticks([1,2,3,4,5])

ax.axvline(mean_rate, ls='--', color='r', label=str(mean_rate))
ax.axvline(mean_rate + mean_rate_std, ls='--', color='g', label=str('+std'))
ax.axvline(mean_rate - mean_rate_std, ls='--', color='g', label=str('-std'))

#ax.set_xlabel(str(mean_rate), color='r')

fig.show()


# ------------------------------------------------------------------------------------------------------------------

# # preliminary conclusions about the data

# For binary descision - 2.8 might be used for Like/Dislike dession 

# sof

