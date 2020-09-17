import math

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def bubbleSort(A):
    for i in range(0, len(A)):
        for j in reversed(range(i+1, len(A))):
            if A[j] < A[j-1]:
                swap(A, j, j-1)

def main():
    A = [4,6,2,7,8,3,6,76,98,1,5,9]
    print(A)
    bubbleSort(A)
    print(A)

if __name__ == "__main__":
    main()