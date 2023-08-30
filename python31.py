import pandas as pd
import numpy as np
#
#my_dict = {"jamess":50, "Lars":60}
##pd.Series(my_dict)
#
#name_list= ["kaan","lars","kirk","rob"]
#new_numppy_array=[10,20,30,40]
#my_series = pd.Series(data=new_numppy_array,index=name_list)
#print(my_series)

my_data = np.array([[10,20,30],[20,30,40],[20,50,10],[10,15,20]])
#print(my_data)
my_names=["james","lars","kirk","rob"]
my_colums=["jan","feb","mar"]

my_data_frame = pd.DataFrame(my_data)
#print(my_data_frame)

new_data_frame = pd.DataFrame(my_data, index=my_names,columns=my_colums)


