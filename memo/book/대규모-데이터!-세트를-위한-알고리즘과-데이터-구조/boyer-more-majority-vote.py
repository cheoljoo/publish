def majority(A):
    index = 0
    count = 1
    for i in range(len(A)):
        if A[i] == A[index]:
            count += 1
        else :
            count -= 1
        if count == 0:
            index = i
            count = 1
    return A[index]

A = [4,5,5,4,6,4,4]
print(majority(A))