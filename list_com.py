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