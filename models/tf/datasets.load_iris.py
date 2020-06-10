from sklearn import datasets
from pandas import DataFrame
import pandas as pd

x_data = datasets.load_iris().data
y_data = datasets.load_iris().target
print(x_data)
print(y_data)
# x_data = DataFrame(x_data,columns=["花萼长度","花萼宽度","花瓣长度","花瓣宽度"])
# pd.set_option("display.unicode.east_asian_width",True)
# print(x_data)
# x_data["class"] = y_data
# print(x_data)