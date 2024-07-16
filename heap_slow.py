import math
# slow heap creation

def pq_parent(n):
    if n == 1:
        return -1
    else:
        return int(math.floor(n/2))

def pq_young_child(n):
    return int(math.floor(2 * n))

def pq_swap(q, p, parent):
    item = q['q'][p]
    q['q'][p] = q['q'][parent];
    q['q'][parent] = item

def bubble_up(q, p):
    if pq_parent(p) == -1:
        return
    #min-heap max-heap
    if q['q'][pq_parent(p)] > q['q'][p]:
        pq_swap(q, p, pq_parent(p))
        bubble_up(q, pq_parent(p))
        
def pq_insert(q, x):
    q['n'] = q['n'] + 1
    q['q'].insert(q['n'], x)
    bubble_up(q, q['n'])
        
def pq_init(q):
    q['n'] = -1

def make_heap(q, s, n):
    iint = 0
    pq_init(q)
    while i < n:
        pq_insert(q, s[i])
        i = i + 1

def bubble_down(q, p):
    c:int
    i:int = 0
    min_index:int

    c = pq_young_child(p)
    min_index = p


def extract_min(q):
    min = -1
    if q['n'] == 0:
        return
    else:
        min = q['q'][0]
        q['q'][0] = q['q'][q['n']]
        q['n'] = q['n'] - 1
        bubble_down(q, 1)

array = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]

def heapsort(s, n):
    i:int = 0
    q = {
        'n': 0,
        'q': []
    }
    while i < n:
        s[i] = extract_min(q)
        i = i + 1
    return q
    
priority_queue = heapsort(array, 20)
print(priority_queue)
