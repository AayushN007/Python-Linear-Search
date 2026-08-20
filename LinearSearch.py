def l_search(arr,key):
    for i in range(1, len(arr)):
        if arr[i] == key:
            return i
    return -1

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    key = 30
    index = l_search(arr,key)
    print(index)