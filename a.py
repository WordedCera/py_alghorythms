op = open('input.txt', 'r')
words = op.read().split()
op.close()

a = words[0]
b = words[1]

def sum_logic(first,second):
    c = int(first) + int(second)
    return c

wr = open('output.txt', 'w')
wr.write(str(sum_logic(a,b)))