# slow heap creation
def pq_parent(n):
    if n == 1:
        return -1
    else:
        return n/2

def pq_young_child(n):
    return 2 * n


def bubble_up(q, p):
    if pq_parent(p) == -1:
        return;
    #if q['q'][pq_parent(p)] > q['q']q[p]:
        #pq_swap(q, p, pq_parent(p))
        #bubble_up(q, pq_parent(p))
        
def pq_insert(q, )
        
def pq_init(q):
    q['n'] = 0

def make_heap(q, s, n):
    i = 0
    pq_init(q)
    print(q)
    while i < n:
        pq_insert(q, s[i])
        i = i + 1

priority_queue = {}
heap = []
    
make_heap(priority_queue, heap, 20)
