def get_max(arr: list):
    for i in range(1,len(arr)):
        if arr[i] <= arr[i-1]:
            tmp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = tmp
    return arr[-1]

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(get_max(arr))
