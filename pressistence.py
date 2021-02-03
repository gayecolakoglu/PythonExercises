def persistence(a):
    total=0
    while a>=10:
         count=1
         total+=1
         for i in str(a):
            count=count*int(i)
            a=count
    return count,total
print(persistence(999))

