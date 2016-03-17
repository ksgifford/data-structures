# data-structures

This repository contains sample code for a number of classic data structures
implemented in Python.

Use the Doubly Linked List or cases where a user may need to reference a
previous item in the list from any given item, or where a user may need to
iterate through the list in reverse order. Otherwise, use the slightly faster
Singly Linked List.

Singly Linked List:
    Module linked_list.py contains a recursively generated linked list class
    (Linked_List).

Stack:
    Module stack.py leverages the linked_list module to build methods for
    generating a stack, as well as adding and removing items.

Doubly Linked List:
    Module dbl_linked_list.py contains a DblLinkedList class with pop, shift,
    insert, append and remove methods. It also contains a Node class, which
    DblLinkedList uses to hold its values.

Queue:
    Module new_queue.py contains a Queue class with enqueue, dequeue, and size
    methods, as well as a peek method that allows the user to get the value of
    the next item in the queue without popping it. The Queue class imports the
    DblLinkedList class described above, and most of its methods are composed
    from this class.

Deque:
    Module new_deque.py contains a Deque class with methods for appending to
    both ends of the deque, removing items from each end of the deque, "peeking"
    at the values of the items on each end, and calculating the size of the
    deque. The Deque class imports the DblLinkedList class, and most of its
    methods are composed from this class.

BinHeap:
    Module binheap.py contains a BinHeap class which sorts itself in binary
    heap fashion. Each node has two children, both of which must be of lesser
    value than the parent. The class has a pop method which removes the root
    at the top of the heap, and a push which appends a new value to the end
    of the heap. In both cases, the heap immediately re-arranges itself.

PriorityQueue:
    Module priorityq.py defines a PriorityQ class which sorts contents by
    the priority with which they were added. In Queue style, it then orders
    items by the order in which they were added (first in, first out).
    It has an insert method to add to the Priority Queue, and a pop method
    to remove and return the first item by priority. The peek method shows
    this same value.

Resources:

    https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python

    http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html

    http://stackoverflow.com/questions/31333462/finding-the-length-of-a-linked-list-in-python

    https://en.wikipedia.org/wiki/Linked_list
