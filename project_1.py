# -*- coding: utf-8 -*-
"""Project 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a0cvtblKOMXv24jpXresbUWbqPSRjgkI

# Libraries
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""# Data Read"""

df = pd.read_csv('https://raw.githubusercontent.com/CunyLaguardiaDataAnalytics/datasets/master/2014-15_To_2016-17_School-_Level_NYC_Regents_Report_For_All_Variables.csv')

df

df.info()

"""#Data Cleaning"""

df.isnull().sum()

df['Regents Exam'].unique()

df=df.dropna()

df.isnull().sum()

df

df.sort_values(by='Mean Score', ascending=False)

df.replace({"s": np.nan, "na": np.nan}, inplace=True)

df

df.dropna(inplace=True)

df

df.isnull().sum()

df.info()

#some columns need to be converted to numeric from object
cols=[
    'Mean Score',
    'Number Scoring Below 65',
    'Percent Scoring Below 65',
    'Number Scoring 65 or Above',
    'Percent Scoring 65 or Above',
    'Number Scoring 80 or Above',
    'Percent Scoring 80 or Above',
    'Number Scoring CR',
    'Percent Scoring CR'
]

for col in cols:
    df[col]=pd.to_numeric(df[col],errors='coerce')

df.info()

df["borough"] = df["School DBN"].str[2]

df.head()

# convert borough_code values into borough names
borough_map = {
    "M": "Manhattan",
    "X": "Bronx",
    "K": "Brooklyn",
    "Q": "Queens",
    "R": "Staten Island"
}

df["borough"] = df["borough"].map(borough_map)

df.head()

"""# Picking School and Feature"""

df[df['School DBN'].str.contains('Q')]['School DBN'].unique()

#picking a school
pick_school = '24Q457'
pick_school_df = df[df['School DBN'] == pick_school]

pick_school_df

#pick feature
feature = 'Mean Score'

"""# Analysis

"""

# Get unique years
years=df['Year'].unique()

#Get unique Regents Exam
regs=df['Regents Exam'].unique()
regs

queens_df = df[df['borough']=="Queens"]

# Create a color palette dictionary
palette_colors = {
    'All School': '#1e81b0',
    'Queens School': '#e28743',
    'School ' + pick_school: '#5D9222'
}

# Create the bar plot
sns.barplot(
    x=['All School', 'Queens School', 'School ' + pick_school],
    y=[df[feature].mean(), queens_df[feature].mean(), pick_school_df[feature].mean()],
    hue=['All School', 'Queens School', 'School ' + pick_school],  # Assign x to hue
    palette=palette_colors,  # Use the color palette dictionary
    dodge=False,  # Prevent dodging of bars (optional)
    legend=False  # Disable the legend
)

plt.title('All School vs Queens School vs Pick School Comparison')
plt.ylabel('Test Score')
plt.show()

"""Here we can see School 24Q457's avegrage mean score is lower than all school system and also all queens schools system."""

year=2017
reg='Common Core Algebra'
sns.barplot(
    x=['All School', 'Queens School', 'School '+pick_school],
    y=[
        df[(df['Year']==year) & (df['Regents Exam']==reg)][feature].mean(),
        queens_df[(queens_df['Year']==year) & (queens_df['Regents Exam']==reg)][feature].mean(),
        pick_school_df[(pick_school_df['Year']==year) & (pick_school_df['Regents Exam']==reg)][feature].mean()
      ],
    hue=['All School', 'Queens School', 'School '+pick_school],  # Assign x to hue
    palette=palette_colors,
    dodge=False,  # Prevent dodging of bars (optional)
    legend=False  # Disable the legend

    )
title=reg+' of year '+ str(year)
plt.title( title)
plt.ylabel('Test Score')
plt.show()

"""For Common core algebra of year 2017 School 24Q457's perpormance is below average."""

for year in years:
  print("Year",year,":")
  for reg in regs:
    sns.barplot(
        x=['All School', 'Queens School', 'School '+pick_school],
        y=[
            df[(df['Year']==year) & (df['Regents Exam']==reg)][feature].mean(),
            queens_df[(queens_df['Year']==year) & (queens_df['Regents Exam']==reg)][feature].mean(),
            pick_school_df[(pick_school_df['Year']==year) & (pick_school_df['Regents Exam']==reg)][feature].mean()
          ],
        hue=['All School', 'Queens School', 'School '+pick_school],  # Assign x to hue
        palette=palette_colors,
        dodge=False,  # Prevent dodging of bars (optional)
        legend=False  # Disable the legend

        )
    title=reg+' of year '+ str(year)
    plt.title( title)
    plt.ylabel('Test Score')
    plt.show()

"""After seeing all Regents Exam of all the years, we can decide that school 24Q457's performance is below average."""

