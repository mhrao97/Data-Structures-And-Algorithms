# Problem 6 - Union and Intersection
import sys
sys.path.append("c:/Users/M/Anaconda3/Lib/site-packages/")

# Your work here

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def convert_list_to_set(llist):
    list_as_set = set()
    element = llist.head
    while element is not None:
        list_as_set.add(element.value)
        element = element.next
    return list_as_set


def union(llist_1, llist_2):
    # Your Solution Here
    union_list = LinkedList()
    for i in convert_list_to_set(llist_1):
        union_list.append(i)

    for i in convert_list_to_set(llist_2):
        union_list.append(i)

    return union_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    # inter_list = set()
    list1 = convert_list_to_set(llist_1)
    list2 = convert_list_to_set(llist_2)
    single_set = list1.intersection(list2)
    inter_list = LinkedList()
    for item in single_set:
        inter_list.append(item)
    return inter_list

# Test case 1
print("---- Test Case 1-----")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Union of linked list 1 and 2")
print(union(linked_list_1, linked_list_2))

print("Intersection of linked list 1 and 2")
print(intersection(linked_list_1, linked_list_2))

# Test case 2

print("-----------Test Case 2----------")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Union of linked list 3 and 4")
print(union(linked_list_3, linked_list_4))

print("Intersection of linked list 3 and 4")
print(intersection(linked_list_3, linked_list_4))

# Test case 2

print("-----------Test Case 3----------")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("Union of linked list 5 and 6")
print(union(linked_list_5, linked_list_6))

print("Intersection of linked list 5 and 6")
print(intersection(linked_list_5, linked_list_6))

# the test cases should print the following:
"""
---- Test Case 1-----
Union of linked list 1 and 2
65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 21 -> 32 -> 1 -> 4 -> 6 -> 9 -> 11 -> 21 -> 
Intersection of linked list 1 and 2
4 -> 21 -> 6 -> 
-----------Test Case 2----------
Union of linked list 3 and 4
65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
Intersection of linked list 3 and 4

-----------Test Case 3----------
Union of linked list 5 and 6
1 -> 
Intersection of linked list 5 and 6

"""