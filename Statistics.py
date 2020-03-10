try:
    i = 1
    while True:
        arr = list(map(int, input().split()))
        print("Case {}: {} {} {}"
              .format(i, min(arr[1:]), max(arr[1:]),
                    max(arr[1:])-min(arr[1:])))
        i+=1
except:
    pass
