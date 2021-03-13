# numpy, pandas, matplotlib practice

# Watch those materials if possible

# numpy tutorial: https://www.w3schools.com/python/numpy_intro.asp

# pandas tutorial: https://www.youtube.com/watch?v=PfVxFV1ZPnk

# funtional programming youtube video: https://www.youtube.com/watch?v=goypZR_lQ7I

# matplotlib tutorial: https://matplotlib.org/tutorials/index.html

# practice:

# 首先熟悉resources 下面是不同的人对于不同APP内容的评分，分别存储在几个不同的文件里。每个文件头上是各个栏的TITLE。
# 其次通过数据处理，进行数据的合并，生成一个EXCEL表格，将用户评分的如下信息列出来。注意有的客户可能对几个不同的内容打分，并且有可能对同一个内容进行多次评分。
# EXCEL表格内容包括  用户基本信息
# 通过图标进行一些简单的数据分析，例如，什么从用户角度，什么职业的人最多，用户评分最多是什么类别，再比如，从内容角度，哪种类目最受欢迎，等等* (try yourself)

#取余操作
import pandas as pd
def simplify(x):
    x=x%19
    return x

def De_duplication():
    df.drop_duplicates(subset=['userid', 'itemindex','rating'], keep='first', inplace=True)


#读取excel表格
df = pd.read_csv("customers_rating_data/u.data.csv")
pf = pd.read_csv("customers_rating_data/u.item.csv")
tf = pd.read_csv("customers_rating_data/u.user.csv")

#数据预处理

#按照userid升序排序
df=df.sort_values(by='userid')

#去除重复评分
De_duplication()

#将itemindex取余处理，以便对应itemtype
df["itemindex"]=df.apply(lambda x:simplify(x["itemindex"]),axis=1)

#将修改保存到excel文件中
df.to_csv('customers_rating_data/u.data.csv', index=False, encoding='utf-8_sig')

#合并多个表并删除多余数据
new = pd.merge(df,pf,on='itemindex')
final = pd.merge(new,tf,on='userid')
final = final.drop(columns = ['itemindex'])
t = final['timestamp']
final = final.drop(columns = ['timestamp'])
final.insert(7,'timestamp',t)
final.to_csv('customers_rating_data/final_data.csv', index=False, encoding='utf-8_sig')
























