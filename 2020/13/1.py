d = []
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        if i == 0:
            continue
        for ind, line in enumerate(l.split(",")):
            if line == "x":
                continue
            line = int(line)
            d.append( (ind, line))
# d = [ (3, 5), (1, 7), (6, 8) ]
bs = []
ns = []
for b, n in d:
    bs.append(n-b)
    ns.append(n)

N = 1
for n in ns:
    N *= n

finals = []

for i, (b, n) in enumerate(d):
    ni = int(N/n)
    for xi in range(1, 10000000):
        if (ni*xi) % n == 1:
            break
    f = (bs[i], ni, xi, bs[i]*ni*xi)
    print(f)
    finals.append(f)
X = 0
for o in finals:
    X += o[-1]

print(X, N)
print(X % N )