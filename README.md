# crawl_assert

这个 toy tool 用于爬取浏览 assert 网站的论文题目和链接，共 10 篇，这些都是在 arxiv 上热度前 10 的论文。本人属于标题党也懒，除了感兴趣的及符合研究领域的论文，其他都没有耐心看，所以简单写了一个爬虫，用于浏览论文标题，感兴趣的再跳转链接去看更多细节。

### 前提

+ 在 Anaconda 中创建 `scrapy` 环境

+ 安装 `scrapy`
+ 安装 `pandas`

### 使用


1. 将 readOrNot.py 复制到 `C:/User/Username` 目录下
2. 注意代码中的路径
3. 打开 `CMD `
3. 激活环境 `activate scrapy`
4. 运行 `python readOrNot.py`

### 功能

1. 爬取完后显示 10 篇论文的标题，询问是否感兴趣

2. 感兴趣的话，就输入对应的数字标号，然后询问是否查看更多细节

3. 回复 “yes” 后，自动跳转网页链接



