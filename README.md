# xxx仓库bug和commit情况分析

数据源 [github](https://github.com/)

## 项目流程
### 题目理解
操作：选择一个具有分析意义的github仓库，通过分析其bug和commit得到该仓库的演化规律。 <br>

### 数据采集与预处理
操作：数据采集与数据预处理
* 利用github api采集信息
* 有效信息提取
* json转csv
* 时间信息处理 <br>

文件：spider.py,clean.py <br>
数据：

| file         | content        |
| ------------ | -------------- |
| issues.json  | issues原始数据 |
| data_all.csv | 转换后的数据   |

### bug情况分析
操作： <br>
文件：analysis.py 、demo.ipynb <br>
数据：

| file | content |
| ---- | ------- |

### commit情况分析
操作： <br>
文件：analysis.py 、demo.ipynb <br>
数据：

| file | content |
| ---- | ------- |

### 特征构建

### 训练与验证
操作：切分数据集，划分训练集、验证集、测试集，选择模型，模型训练，进行模型调整。 <br>
文件： <br>

### 模型选择
xxx模型 

### 模型预测
操作：用训练好的模型进行预测 <br>
文件： <br>
数据： 

| file 		| content		| 
| :-------:	| :-------:	| 
| xxx.csv	| 预测结果	| 