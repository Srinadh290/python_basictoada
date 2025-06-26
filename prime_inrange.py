#prime in range
def is_prime(index):
    if index<2:
        return False
    for i in range(2,(int(index**0.5))+1):
        if index%i==0:
            return False
    return True
def in_range(start,end):
    list1=[]
    for i in range(start,end):
        if is_prime(i):
            list1.append(i)
    return list1
print(in_range(1,100))