import sys

data = sys.stdin.readlines()[1:]
data.sort(key=lambda x:int(x.split()[0]))

print("".join(data))