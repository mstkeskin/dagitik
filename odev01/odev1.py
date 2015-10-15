import numpy as np
import matplotlib.pyplot as plt

m1,q1=5,1
m2,q2=3,0.75

x1=np.random.normal(m1,q1,10000)
x2=np.random.normal(m2,q2,10000)

for n in range(len(x1)):
    x1[n]=round(x1[n])

for n1 in range(len(x2)):
    x2[n1]=round(x2[n1])



Histogram=[]

index=-20


while True:

    find=0
    for elem in x1:

            if elem  == index:
                find += 1
    Histogram.append(find)
    index +=1



    if index >20:
        break
Histogram1=[]


index1=-20

while True:

    find1=0
    for elem1 in x2:

            if elem1  == index1:
                find1 += 1
    Histogram1.append(find1)
    index1 +=1




    if index1 >20:
        break
b=sum(int(i) for i in Histogram)
c=sum(int(i) for i in Histogram1)
print "x1",x1
print "Histogram",Histogram
print "x2",x2
print "Histogram1",Histogram1



for t in range(len(Histogram)):
    Histogram[t]=Histogram[t]/float(b)

for t1 in range(len(Histogram1)):
    Histogram1[t1]=Histogram1[t1]/float(c)

print "Normalize Histogram",Histogram

print "Normalize Histogram1",Histogram1

#plt.hist(range(-20,21),40,weights=Histogram,color='blue')


#plt.hist(range(-20,21),40,weights=Histogram1,color='red')

plt.axis(-20,20,0,1)
plt.bar(range(-20,21), Histogram,color='blue')
plt.bar(range(-20,21),Histogram1,color='red')


plt.show()

j=0
k=0
total=0
while j<40 and k<40:
    if Histogram[j]==0:
        j +=1
        continue
    if Histogram1[k]==0:
        k +=1
        continue
    if Histogram[j]<Histogram1[k]:
        total=Histogram[j]*abs(k-j)+total
        Histogram[j]=0
        Histogram1[k]=Histogram1[k]-Histogram[j]
        continue
    if Histogram[j]>=Histogram1[k]:
        total=Histogram1[k]*abs(k-j)+total
        Histogram1[k]=0
        Histogram[j]=Histogram[j]-Histogram1[k]
        #Histogram1[k+1]=Histogram1[k]+(Histogram[j]-Histogram1[k])
        continue


print "Total=",total
