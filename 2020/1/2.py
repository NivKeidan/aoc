import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import bubblesort

arr = []
ht = {}

with open('inp1') as f:
    for l in f.readlines():
        l = l.strip()
        n = int(l)
        arr.append(n)
        ht[n] = True
bubblesort.sort(arr)

for i, current in enumerate(arr):
    for next in arr[i+1:]:
        print("current %d, next %d" % (current, next))
        midSum = current + next
        if midSum > 2020:
            break
        goal = 2020-midSum
        if goal in ht:
            print(goal * current * next)
            exit(0)