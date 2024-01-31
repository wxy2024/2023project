# github pandas仓库issues和commits情况分析

数据源 [github](https://github.com/)

## 项目流程
### 题目理解
操作：选择一个具有分析意义的github仓库，通过分析其issues和commits得到该仓库的演化规律。 <br>

### 数据采集与预处理
操作：数据采集与数据预处理
* 利用github api采集信息（repo token）
* 有效信息提取
* json转csv
* 时间信息处理 <br>

代码：

| file | content |
| ---- | ------- |
| spider.py  | github api 提取数据 |
| clean_tocsv.py  | 提取有效信息并转为csv |

数据：

| file         | content        |
| ------------ | -------------- |
| issues.json  | issues原始数据 |
| commits.json  | commits原始数据 |
| issues_all.csv | issues转换后的数据 |
| commits_all.csv | commits转换后的数据   |


### issues情况分析
操作：issues数量统计与趋势分析、issues类型分析、issues修复时间分析 <br>
代码：

| file | content |
| ---- | ------- |
| issues分析.ipynb | 挖掘分析issues规律并可视化 |

图片：

| file | content |
| ---- | ------- |
| all_issues_num -- date.png | issues创建总数量与关闭总数量随日期变化规律 |
| created&closed_issues_num -- date(month).png | 每月issues创建数量与关闭数量变化规律 |
| created&open_issues_num,percentage -- date(month).png | 每月仍未解决的issues占总数量比例变化规律 |
| time to resolve issues -- date.png | issues解决时间随日期变化规律 |
| issues type.png | issues类型分析 |
| update time.png | issues更新时间分析 |


### commits情况分析
操作： commits数量统计与趋势分析、commits类型分析、commits修复时间分析<br>
代码：

| file | content |
| ---- | ------- |
| commits分析.ipynb | 挖掘分析commits规律并可视化 |

图片：
| file | content |
| ---- | ------- |

<!-- 

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
| xxx.csv	| 预测结果	|  -->