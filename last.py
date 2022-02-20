op = open('input.txt', 'r')
words = op.read().split()
op.close()

if words and len(words) > 1:
     j = words[0]
     s = words[1]
else:
    j = 'a'
    s = 'b'

def compare_count(first_ch, second_ch):
    counter = 0
    for letter in second_ch:
        if letter in first_ch:
            counter += 1
    return counter

wr = open('output.txt', 'w')
wr.write(str(compare_count(j,s)))
wr.close()