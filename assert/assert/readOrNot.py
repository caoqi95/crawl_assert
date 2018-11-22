# -*- coding: utf-8 -*-
import pandas as pd
import webbrowser
import time
import os

# 进入爬虫所在的路径
os.chdir("D:/cao/scrapy/assert/assert")

# 打印文件目录
ret= os.getcwd()
print("Now is in " + str(ret))
print("Start crawling..... ")

# 延时 3 秒
time.sleep(3)

# 输入命令，爬取论文
os.system("scrapy crawl assert_spider -o paper.csv")

# 读取爬取的论文结果
df = pd.read_csv("paper.csv")

# 打印各个论文题目
print("-----------------------------------------------------------------------------------------")
for i in range(10):

    print(df['paper'][i])
    print("-----------------------------------------------------------------------------------------")

# 询问是否有感兴趣的论文
num = input("Which paper do you want to read : ")

if num == 'none' or int(num) == 0:
    os.system("exit")

else:
    # 询问是否查看更多细节
    detail = str(input("Do you want to see more details?  - "))

    # 回答 yes 即打开论文详情网页
    if detail == "yes":
        webbrowser.open(df['url'][int(num)])

