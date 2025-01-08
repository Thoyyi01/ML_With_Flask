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