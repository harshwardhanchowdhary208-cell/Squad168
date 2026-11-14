def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    n = int(input())                    # input size
    arr = list(map(int, input().split()))[:n]  # input elements

    bubbleSort(arr)                     # function call

    print(*arr)                         # output

if __name__ == "__main__":
    main()
