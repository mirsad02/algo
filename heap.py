import math

# heap logic

def pq_parent(n):
    if n == 0:
        return -1
    else:
        return int(math.floor(n/2))

def pq_young_child(n):
    return int(math.floor(2 * n))

def pq_swap(q, p, parent):
    item = q['q'][parent] 
    q['q'][parent] = q['q'][p]
    q['q'][p] = item

def bubble_up(q, p):
    parent = pq_parent(p)
    if parent == -1:
        return
    # min-heap max-heap
    if q['q'][parent] > q['q'][p]:
        pq_swap(q, p, parent)
        bubble_up(q, parent)

def pq_insert(q, x):
    q['n'] = q['n'] + 1
    q['q'].insert(q['n'], x)
    bubble_up(q, q['n'])
    
def pq_init(q):
    q['n'] = -1

# slow heap creation

def make_heap(q, s, n):
    i:int = 0
    pq_init(q)
    while i < n:
        pq_insert(q, s[i])
        i = i + 1

def bubble_down(q, p):
    c:int
    i:int = 0
    min_index:int = p

    c = pq_young_child(p)
    min_index = p

    while i <= 1:
        if c + i <= q['n']:
            if q['q'][min_index] > q['q'][c + i]:
                min_index = c + i
        i = i + 1

    if min_index != p:
        pq_swap(q, p, min_index)
        bubble_down(q, min_index)

# fast heap creation 

def make_heap_fast(q, s, n):
    i:int = -1
    q['n'] = n

    while i < n:
        pq_insert(i + 1, s[i])
        i = i + 1

    j:int = q['n'] / 2

    while j >= 0:
        bubble_down(q, i)
        j = j - 1

# extracting the minimum

def extract_min(q):
    min = -1
    if q['n'] == -1:
        return
    else:
        min = q['q'][0]
        q['q'][0] = q['q'][q['n']]
        q['n'] = q['n'] - 1
        bubble_down(q, 0)
    return min

array = [ 20, 19, 18, 17, 16, 15, 14, 13 ]

def heapsort(s, n):
    i:int = 0
    q = {
        'n': 0,
        'q': []
    }
    make_heap(q, s, n)
    while i < n:
        s[i] = extract_min(q)
        i = i + 1
    return {
        'q': q,
        's': s
    }

priority_queue = heapsort(array, 8)
print(priority_queue)

# heap compare

def heap_compare(q, i, count, x):
    if count <= 0 or i > q['n']:
        return count
    if (q['q'][i] < x):
        count = heap_compare(q, pq_young_child(i), count - 1, x)
        count = heap_compare(q, pq_young_child(i) + 1, count - 1, x)    
    return count
