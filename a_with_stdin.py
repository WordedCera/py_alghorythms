import sys

arr = []

for line in sys.stdin.readline().split():
    arr.append(line.strip())

a = arr[0]
b = arr[1]

def sum_logic(first, second):
    c = int(first) + int(second)
    return c

print(sum_logic(a,b))