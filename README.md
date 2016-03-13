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

Parenthetics:
    Module parenthetics_kevin.py contains a test for evaluating strings that
    contain parenthetical statements to ensure proper opening and closing of
    parentheses. Properly formatted strings will return a value of 0. Strings
    with hanging open parentheses will return a value of 1. Strings with extra
    closing parentheses, or a closing parenthesis that has not been preceded by
    an opening parenthesis, will return a value of -1.


Resources:

    https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python

    http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html

    http://stackoverflow.com/questions/31333462/finding-the-length-of-a-linked-list-in-python

    https://en.wikipedia.org/wiki/Linked_list
