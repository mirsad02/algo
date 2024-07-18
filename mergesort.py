import math

# mergesort

def headq(buffer):
    return buffer[0]

def empty_queue(buffer):
    return len(buffer) == 0

def enqueue(buffer, x):
    buffer.insert(0, x)

def dequeue(buffer):
    return buffer.pop(0)
    
def init_queue():
    return []

def merge(s, low:int, middle:int, high:int):

    i:int = low
    j:int = middle + 1
    buffer1 = init_queue()
    buffer2 = init_queue()

    while i <= middle:
        enqueue(buffer1, s[i])
        i = i + 1

    while j <= high:
        enqueue(buffer1, s[j])
        j = j + 1

    k:int = low
    while empty_queue(buffer1) == False or empty_queue(buffer2) == False:
        if headq(buffer1) <= headq(buffer2):
            s[k + 1] = dequeue(buffer1)
        else:   
            s[k + 1] = dequeue(buffer2)
    
    while empty_queue(buffer1) == False:
        s[k + 1] = dequeue(buffer1)

    while empty_queue(buffer2) == False:
        s[k + 1] = dequeue(buffer2)
    
array = [ 20, 19, 18, 17, 16, 15, 14, 13 ]

def mergesort(s, low:int, high:int):
    middle:int
    if low < high:
        middle = int(math.floor((low + high) / 2))
        mergesort(s, low, middle)
        mergesort(s, middle + 1, high)
        merge(s, low, middle, high)
 
mergesort(array, 0, 7)

print(array)
