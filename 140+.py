'''a=str(input())
b=""
for i in a:
    if ord(i)%2==0:
        b+=i.upper()
    else:
        b+=i.lower()
    print(b)



a=str(input())
c=input()
b='aieou'
d=""
for i in a:
    if i in b:
        d+=c
    else:
        d+=i
        print(d)



a=input().split()
b={}
for i in a:
    b[i]=i.upper()
    print(b)


a=input().split()
b,c,d=a
if b==c==d:
    print("3")
elif b==c or c==d or d==b:
    print("2")
else:
    print("0")


a=list(map(int,input().split()))
b,c,d=a
e=sorted(a)
if (e[0]**2 + e[1]**2 == e[2]**2):
        print("working")
else:
        print("not working")



a=input().split()
a.sort()
print(a)





a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
d=set(b)
e=set(c)
f=d.symmetric_difference(e)
print(list(f))






a=str(input())
b=''
for i in a:
    c=int(i)**2
    b+=str(c)
    print(b)




a=str(input())
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        print("true")
    else:
        print("false")



a=str(input())
b=a.lower()
c=""
for i in b:
    if i not in c:
        c+=i
if c==a:
    print("true")
else:
    print("False")




a=input().split()
b=''
for i in a:
    b+=i[0]
    print(b)




a=list(map(int, input().split()))
b,c,d=a
e=[num for num in range(b,c+1) if num%d==0]
print(e)




a=input().split()
b=[]
for i in a:
    if i.isnumeric():
        b.append(i)
        print(b)






a=list(map(int, input().split()))
b=[]
for i in range(len(a)):
    b.append(a[i]+i)
    print(b)





a=int(input())
b=[]
for i in range(1,a+1):
    if i%2==0:
        b.append(i)
        print(b)




#index_of_caps("eDaBiT") ➞ [1, 3, 5]


a=str(input())
b=[]
index=0
for i in a:
    if i.isupper():
        b.append(index)
    index+=1
    print(b)



#double_char("String") ➞ "SSttrriinngg"



a=str(input())
b=""
for i in a:
    b=b+i*2
    print(b)



#move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]

a=list(map(int,input().split()))
b=int(input())
c=[]
d=[]
for i in a:
    if i!=b:
        c.append(i)
    else:
        d.append(i)
c.extend(d)
print(c)





n=int(input())
fact=1
if n==0:
    print("1")
elif n<0:
    print("not possible")
for i in range(1,n+1):
    fact*=i
    print(fact)




a=str(input())
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
    print(b.swapcase())




# hamming Distnce

a=str(input())
b=str(input())
c=0
if len(a)!=len(b):
    print("Error")
else:
    for i in range(len(a)):
        if a[i]!=b[i]:
            c+=1
    print(c)



M=str(input())
if M == "rock":
    winning_move = "paper"
elif M == "paper":
    winning_move = "scissors"
elif M == "scissors":
    winning_move = "rock"
else:
    winning_move = "Invalid move"

print(winning_move)




a=str(input())
b='aieou'
c=input()
d=''
for i in a:
    if i in b:
        d+=c
    else:
        d+=i
print(d)




a=list(map(int,input().split()))
b,c,d=a
e=0
for i in range(b,c+1):
    if i%d==0:
        e+=i
        print(e)





a=str(input())
b=a.find("@")
c=a[0:b]
print(c)




#If the following n is given as input to the program:
#8
#Then, the output of the program should be:
#0,1,1,2,3,5,8,13


n=int(input())
a=[0,1]
for i in range(n):
    a.append(a[-1]+a[-2])
    print(a)


n=int(input())
a=[]
for num in range(n + 1):
   if num % 5 == 0 and num % 7 == 0:
      a.append(str(num))
      print(",".join(a))





a=input().split()
b=input().split()
c=input().split()
d=[]
for i in a:
    for j in b:
        for k in c:
            e=f"{i} {j} {k}"
            d.append(e)
print(d)




a=int(input())
n=list(map(int,input().split()))
count=0
a=0
for i in range(1,10000):
    if i**2 in n:
        count+=1
    else:
       a+=1
print(count)


a=list(map(int,input().split()))
b=sorted(a)
c=b[-1]
d=a.index(c)
print(c,d)



a=[1,2,4,43,2,3,432,32,1]
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
    print(b)



n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
c=b.sort()
d=b[-2]
print(a.count(d))



S=str(input())
K=int(input())
for i in range(len(S) - K + 1):                  # 5-3+1 =3
        substring = S[i:i + K]
        print(substring)



# Armstrong Number
a=str(input())
b=len(a)
d=0
for i in a:
    c=int(i)
    d+=c**b
    if int(a)==d:
      print("Armstrong")
      break
else:
      print("Not Armstrong")



n=int(input())
a=list(map(int,input().split()))
sum=32
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] + a[j] ==sum:
            print(a[i],a[j])



a=int(input())
b=int(input())
for i in range(0,a+1):
    for j in range(1,i+1):
       print(i+j,end='  ') 
    print()     



n=int(input())
sum=''
while n>0:
    sum+=str(n%2)
    n=n//2
for i in range(len(sum)-1,-1,-1):
    print(sum[i],end=' ')




# To print the string removing the vowels between the two consonant letters.
a=str(input())
d=len(a)
b='aieouAIEOU'
c=a[0]
for i in range(1,len(a)-1):
    if(a[i] in b and a[i+1] not in b and a[i-1] not in b):
        continue
    else:
        c+=a[i]
c+=a[d-1]
print(c)







a=int(input())
for i in range(a+1):
    for j in range(i):
        print("*",end=' ')
    print()





a=int(input())
for i in range(a+1):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,a):
        print('*',end=" ")
    print()



a=int(input())
for i in range(a+1):
    for j in range(i,a):
        print("*",end=" ")
    print()





a=int(input())
for i in range(a):
    for j in range(i,a):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()







a=int(input())
for i in range(a):
    for j in range(i,a):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()'''























      
      






    

        





