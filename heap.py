def pq_parent(n):
    if n == 1:
        return 1
    else:
        return n/2

def pq_young_child(n):
    return 2 * n


def bubble_up(q, p):
    

def pq_init(q):
    q['n'] = 0

def make_heap(q, s, n):
    i = 0
    pq_init(q)
    while i < n:
        pq_insert(q, s[i])

