import json
from collections import defaultdict
path = r'E:\数据分析\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
o = open(path)
records = [json.loads(line) for line in o]
# print(records[0])
# print(type(records[0]))


#用python代码对列表中的值进行计数
time_zone = [rec['tz'] for rec in records if 'tz' in rec]

# 1.计算一个列表每个元素出现的次数
from collections import Counter
counts = Counter(time_zone)

#2.计算一个列表每个元素出现的次数
def get_counts(sequence):
    sequence_assemble = {}
    sequence_set = set(sequence)
    for i in sequence_set:
        sequence_assemble[i] = sequence.count(i)
    return sequence_assemble

#3.计算一个列表每个元素出现的次数,from collections import defaultdict
def get_counts(sequence):
    counts =defaultdict(int)    #所有的值会初始化为0
    for x in sequence:
        counts[x] += 1
    return counts


#对字典按值进行排序，如果asd:asd[0]则是按照key排序，reverse是反转，排序后是列表
def dic_sortd(sequence_assemble):
    sequence_assemble = sorted(sequence_assemble.items(),key = lambda asd:asd[1],reverse = True)
    return (sequence_assemble)

#用Pandas的DataFrame读取JSON数据、写入excel、统计每个个体的个数
import pandas as pd
import xlwt
import numpy as np
import matplotlib.pyplot as plt
frame = pd.DataFrame(records)
# print(frame['tz'].value_counts())
clean_tz = frame['tz'].fillna('haha') #替换缺失值
clean_tz[clean_tz == ''] = 'Unknown'  #未知值（空字符串）通过布尔型数组索引加以替换
# 未知值（空字符串）通过数列索引加以替换
# for i in range(0,len(clean_tz)):
#     if clean_tz[i] == '':
#         clean_tz[i] = 'Unknown'
# print(clean_tz.value_counts()[:10])
# clean_tz.value_counts()[:10].plot(kind= 'barh',rot=0)
# plt.show()

#统计大家使用的浏览器的种类
#pandas中也带有统计数列各元素个数的函数，list.value_counts()，返回的是Series
records_browser = pd.Series([i.split(' ')[0] for i in frame['a'] if type(i) == str])
print(records_browser.value_counts()[:10])
(records_browser.value_counts()[:10]).plot(kind = 'barh',rot = 0)
plt.show()
# print(frame_browser)
