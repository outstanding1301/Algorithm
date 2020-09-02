# 삽입정렬

# best case = O(n)
# avg case = O(n^2)
# worst case = O(n^2)

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j] 
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

def main():
    A = [5, 3, 4, 2, 1]
    print(A)
    insertionSort(A)
    print(A)

if __name__ == "__main__":
    main()