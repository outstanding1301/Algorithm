import math


def _mergeSort(A, p, r, B):
    if p < r:
        q = math.floor((p+r)/2)
        _mergeSort(A, p, q, B)
        _mergeSort(A, q+1, r, B)
        merge(A, p, q, r, B)

def mergeSort(A):
    B = [0 for i in range(0, len(A))]
    _mergeSort(A, 0, len(A)-1, B)

def merge(A, p, q, r, B):
    (i, j, k) = (p, q+1, p)
    while k <= r:
        if j > r:
            B[k] = A[i]
            i+=1
        elif i > q:
            B[k] = A[j]
            j+=1
        elif A[i] < A[j]:
            B[k] = A[i]
            i+=1
        else: 
            B[k] = A[j]
            j+=1
        k+=1
    for l in range(p, r+1): A[l] = B[l]

def main():
    A = [4,6,2,7,8,3,6,76,98,1,5,9]
    print(A)
    mergeSort(A)
    print(A)

if __name__ == "__main__":
    main()