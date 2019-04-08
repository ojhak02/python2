##lis=[2,1,3,5,3,8]
##lis.insert(3,4)
##lis.sort()
##print(lis)

lis1=[2,1,3,5]
lis2=[6,4,3]
lis1.extend(lis2)
for i in range(0,len(lis1)):
        print(lis1[i])

lis1.append(lis2)
print(lis1)
