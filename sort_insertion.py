# best time = O(n)
# avg time = O(n^2)
# worst time = O(n^2)

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j] 
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

def main():
    A = [8, 2, 4, 9, 3, 6]
    # output = [2, 3, 4, 6, 8, 9]
    print(A)
    insertionSort(A)
    print(A)

if __name__ == "__main__":
    main()