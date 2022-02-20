j = 'драгоценности'
s = 'камни'

def comparer(first_word, second_word):
    num_of_ch = len(set(first_word) & set(second_word))
    return num_of_ch

print(comparer(j,s))