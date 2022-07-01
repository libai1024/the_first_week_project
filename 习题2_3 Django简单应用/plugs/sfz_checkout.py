numlist = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
str = input()
checknum = ['1','0','X','9','8','7','6','5','4','3','2']
sum = 0
for i in range(len(numlist)):
    sum += numlist[i] *(int(str[i])-int('0'))

if checknum[sum%11] == str[-1]:
    print("OK")
else:
    print("NO")