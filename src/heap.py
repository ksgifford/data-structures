import math
import time


def heapify1(seq):
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


def heapify_outer(seq):
    heap = list(seq)
    print('heapifying:', heap)
    parent = len(heap) - 1

    while parent >= 0:
        heapify_down(heap, parent)
        parent -= 1

    return heap


def heapify_down(heap, parent):
    left = left_child(parent)
    right = right_child(parent)

    largest = parent
    if compare(heap, left, parent):
        largest = left
    if compare(heap, right, largest):
        largest = right

    if largest != parent:
        swap(heap, largest, parent)
        heapify_down(heap, largest)


def parent(idx):
    return int(math.floor((idx - 1) / 2))


def left_child(idx):
    return (idx * 2) + 1


def right_child(idx):
    return (idx * 2) + 2


def swap(heap, idx1, idx2):
    heap[idx1], heap[idx2] = heap[idx2], heap[idx1]
    print('heap after swap: {}'.format(heap))
    # time.sleep(1)


def compare(heap, child_idx, parent_idx):
    # print('comparing child {}  at {} to parent {} at {}'.format(
    #     heap[child_idx], child_idx, heap[parent_idx], parent_idx))
    if child_idx <= 0:
        return False
    try:
        return heap[child_idx] > heap[parent_idx]
    except IndexError:
        return False


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
        result = heapify_outer(t)
        print(result)
        results.append(result)
    for r in results:
        print(r)
