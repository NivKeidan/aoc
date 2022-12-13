# m = {}
arr = []
s = 0
goal = 1639024365
# goal = 127

# def isValid(n):
#     print(m)
#     print("checking for", n)
#     for n2 in arr:
#         req = n-n2
#         print("evaluating", n2, "looking for", req)
#         if req in m:
#             print("found")
#             return True
#     return False

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        n = int(l)
        print(arr)
        arr.append(n)
        s += n
        
        if s == goal:
            print("just calc2")
            arr.sort()
            print("sorted", arr)
            exit()

        while s > goal:
            s -= arr[0]
            arr = arr[1:]
            if s == goal:
                print("just calc")
                arr.sort()
                print("sorted", arr)
                print(arr[0] + arr[-1])
                exit()

        # if i >= 25 and not isValid(n):
        #     print(n)
        #     exit(0)

        # m[n] = True
        # arr.append(n)
        # if i >= 25:
        #     del m[arr[0]]
        #     arr = arr[1:]
        # continue
        