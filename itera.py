rs = lambda x,y:(x+y,x*y)
print(rs(2,4))

"---------------------------------------------"


ls = [i for i in range(1,20)]
a = ls
for i in ls:
    if i<5:
        print(i)
    else:
        break

i=iter(a)
for j in i:
    if j%4==0:
        print(j,end="")

i=iter(a)
for i in iter(a):
    if i%2==0:
        print(i)

#"Check the below list and display the "
#"string where the string letter is start with "a" (OR) contain a "A""

#l = ["aaa","wer","aer","ggt"]


# Generator
def sqr(i):
    for i in range(i):
        i = i+2
        yield i
sqr(10)
for i in sqr(10):
    print(i)