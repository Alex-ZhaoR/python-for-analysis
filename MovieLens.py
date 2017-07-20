#-*- coding: utf-8 -*-
#将各个表读到一个DataFrame中去
import pandas as pd
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table(r'C:\Users\strivezr\Desktop\python for data analysis\ml-1m\users.dat',sep = '::',header=None,names=unames)
rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table(r'C:\Users\strivezr\Desktop\python for data analysis\ml-1m\ratings.dat',sep = '::',header=None,names=rnames)
mnames = ['movie_id','title','genres']
movies = pd.read_table(r'C:\Users\strivezr\Desktop\python for data analysis\ml-1m\movies.dat',sep = '::',header=None,names=mnames)

data = pd.merge(pd.merge(users,ratings),movies)

mean_ratings = data.pivot_table(columns = ['gender'],index = ['title'],values = ['rating'],aggfunc = 'mean')

ratings_by_title = data.groupby('title').size()
print(ratings_by_title)
ratings_bt_title1 =  data['title'].value_counts()
# print(ratings_bt_title1)