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
    i = 0
    pq_init(q)
    while i < n:
        pq_insert(q, s[i])
        i = i + 1

priority_queue = {
    'n': 0,
    'q': []
}
heap = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
    
make_heap(priority_queue, heap, 20)
print(priority_queue)