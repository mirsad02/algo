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
    q['q'].insert(p, q['q'].pop(parent))

def bubble_up(q, p):
    if pq_parent(p) == -1:
        return;
    if q['q'][pq_parent(p)] > q['q']['p']:
        pq_swap(q, p, pq_parent(p))
        print('swap')
        #bubble_up(q, pq_parent(p))
        
def pq_insert(q, x):
    if q['n'] > 99999999999:
        return -1
    else:    
        q['n'] = q['n'] + 1
        q['q'].insert(q['n'], x)
        bubble_up(q, q['n'])
        
def pq_init(q):
    q['n'] = -1

def make_heap(q, s, n):
    i = 0
    pq_init(q)
    while i < n:
        pq_insert(q, s[i])
        i = i + 1

priority_queue = {
    'n': 0,
    'q': []
}
heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
make_heap(priority_queue, heap, 20)
