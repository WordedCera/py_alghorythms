a = [0,1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0]

def vector_counter(dict_object):
    counts = {}
    count = 0
    last_item = None
    for item in dict_object:
        if last_item == item:
            count += 1
        else:
            count = 1
            last_item  = item
        if count > counts.get(item,0):
            counts[item] = count

    return counts[1]

print(vector_counter(a))


