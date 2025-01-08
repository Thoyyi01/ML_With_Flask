res = [i for i in range(0,10)]
print(res)
for i in res:
    if i<5:
        print(i)

print = "------------------------------------------------------"        

t = ["hello","mental"]
m = [i.upper() for i in t]
print(m)


keys = ["name","age","city"]
values = ["Banglore",25,"Hyderabad"]
dictionary = {k:v for k,v in zip(keys,values)}
print(dictionary)

import pandas as pd 
name = ["Thoyyi","Badri","M"]
id = [179,180,195]
phone = [855,584,826,]
dict1={
    "ID":id,
    "Name":name,
    "Phone":phone,
}
M = pd.DataFrame(dict1)
print(M)


import pandas as pd
import numpy as np

internal_marks = [2, 4, 6,]
sleep_hrs = [1, 3, 5,]
stu_name = ["Karthi", "Dev", "Kanguva"]

M = {
    "Student Name!": stu_name,
    "Internal Marks": internal_marks,
    "Sleep Hrs": sleep_hrs
}

df = pd.DataFrame(M)
print(df)
