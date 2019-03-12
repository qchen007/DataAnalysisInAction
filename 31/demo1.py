# coding=utf-8
from efficient_apriori import apriori
# 设置数据集
data = [('牛奶','面包','尿布'),
           ('可乐','面包', '尿布', '啤酒'),
           ('牛奶','尿布', '啤酒', '鸡蛋'),
           ('面包', '牛奶', '尿布', '啤酒'),
           ('面包', '牛奶', '尿布', '可乐')]
# 挖掘频繁项集和频繁规则
itemsets, rules = apriori(data, min_support=0.5,  min_confidence=1)
print(itemsets)

'''itemsets:
{1: {('啤酒',): 3, ('尿布',): 5, ('牛奶',): 4, ('面包',): 4}, 2: {('啤酒', '尿布'): 3, ('尿布', '牛奶'): 4, ('尿布', '面包'): 4, ('牛奶', '面包'): 3}, 3: {('尿布', '牛奶', '面包'): 3}}
'''
print('\r')
print(rules)
'''rules
[{啤酒} -> {尿布}, {牛奶} -> {尿布}, {面包} -> {尿布}, {牛奶, 面包} -> {尿布}]
'''

