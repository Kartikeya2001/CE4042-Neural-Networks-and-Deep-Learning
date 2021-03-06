# -*- coding: utf-8 -*-

import pandas as pd

text_emotion_recognition = pd.read_csv("data/Original Data/text_emotion_recognition.csv")

def dropColumns(df, columns_to_drop): #This function is utilized to drop the specified columns in the columns_to_drop list and returns the dataframe
  for column in columns_to_drop:
    df.drop(column, inplace=True, axis=1)
  return df

def concatenateColumns(df, columns_dict): #This function concatenates 2 columns and then eliminates the NaN value by first converting the contents of required 2 columns to string and then strips contents of column containing 'nan' off, and returns the dataframe
  for key,value in columns_dict.items():
    df[key] = df[key].map(str) + ' ' + df[value].map(str)
    df[key] = df[key].map(lambda x: x.lstrip('nan').rstrip('nan'))
    df[key] = df[key].map(lambda x: x.lstrip(' ').rstrip(' '))
  return df

columns_dict = {'tweet':'content', 'tweettype':'sentiment'}
columns_to_drop = ['id','tweet_id','Unnamed: 0', 'author', 'sentiment', 'score', 'content'] 
text_emotion_recognition = concatenateColumns(text_emotion_recognition, columns_dict)

#This follwoing three lines are error correction step beacuse earlier in the concatenateColumns, we stripped off strings 'nan' from the column tweettype. 
text_emotion_recognition['tweettype'] = text_emotion_recognition['tweettype'].str.replace('ger','anger') 
text_emotion_recognition['tweettype'] = text_emotion_recognition['tweettype'].str.replace('ananger','anger')
text_emotion_recognition['tweettype'] = text_emotion_recognition['tweettype'].str.replace('fu','fun')

author = text_emotion_recognition['author']
score = text_emotion_recognition['score']
text_emotion_recognition.index.name = 'tweet_id'
text_emotion_recognition = dropColumns(text_emotion_recognition, columns_to_drop)
text_emotion_recognition

sentiment_categories = list(text_emotion_recognition['tweettype'].unique())
sentiment_categories

text_emotion_recognition.to_csv('data/Original Data/text_emotion_recognition_updated.csv')

