import math
import time


def heapify(seq):
    heap = list(seq)
    print('heapifying:', heap)
    starting_idx = len(heap) - 1
    idx = starting_idx

    while starting_idx > 0:
        print('\n')
        print('starting: {}; pointer: {}'.format(starting_idx, idx))
        # time.sleep(1)

        while compare(heap, starting_idx, parent(starting_idx)):
            print('starting: {}; pointer: {}'.format(starting_idx, idx))
            # time.sleep(1)

            while compare(heap, idx, parent(idx)):
                print('starting: {}; pointer: {}'.format(starting_idx, idx))
                # time.sleep(1)
                swap(heap, idx, parent(idx))
                idx = parent(idx)

            idx = starting_idx

        starting_idx -= 1
        idx = starting_idx

    return heap


def parent(idx):
    return int(math.floor((idx - 1) / 2))


def swap(heap, idx1, idx2):
    heap[idx1], heap[idx2] = heap[idx2], heap[idx1]
    print('heap after swap: {}'.format(heap))
    # time.sleep(1)



def compare(heap, child_idx, parent_idx):
    print('comparing child {}  at {} to parent {} at {}'.format(
        heap[child_idx], child_idx, heap[parent_idx], parent_idx))
    if child_idx <= 0:
        return False
    return heap[child_idx] > heap[parent_idx]


tests = [
    [0, 0, 0, 0, 0, 0, 1],
    [3, 4, 5],
    [9, 11, 494, 0],
    [1, 2, 3, 4, 4, 5, 6, 6, 8],
    [39383, 9287666, 2, 0, 23, 0, 737338]

]

results = []

if __name__ == '__main__':
    for t in tests:
        result = heapify(t)
        print(result)
        results.append(result)
    for r in results:
        print(r)
