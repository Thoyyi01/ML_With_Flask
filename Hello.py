a = 5
b = 10
a, b = b, a
print(a, b)

#Append
Hi=[1,2,"Amazon","E-Commerce","Website"]
Hi.append(["HYD","BENG"])
print(Hi)

#Insert
Hi.insert(1,"HYD Gachibowli")
print(Hi)

#Extend
m=[1,2,3,4,5]
m.extend([6,7])
print(m)
sum(m)

#POP
m.pop()
print(m)
m.pop(4)
print(m)

#Count
m.count(2)

S = "Hello"
T = 'World!'
result = S+"#"+T
print(result)