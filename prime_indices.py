#prime indices
def is_prime(index):
    if index<2:
        return False
    for i in range(2,(int(index**0.5))+1):
        if index%i==0:
            return False
    return True
def sum_indices(arr):
    total=0
    for i in range(len(arr)):
        if is_prime(i):
            total+=arr[i]
    return total
n=6
arr=[2,5,26,5,4,4]
result=sum_indices(arr)
print(result)