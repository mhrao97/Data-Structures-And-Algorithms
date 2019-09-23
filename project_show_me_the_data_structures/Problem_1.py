# problem 1 - LRU cache

import sys
sys.path.append("c:/Users/M/Anaconda3/Lib/site-packages/")

# Your work here

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.hash_map = {}

        self.head = None
        self.end = None

        self.capacity = capacity
        self.current_size = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]

        if self.head == node:
            return node.value
        self.remove(node)
        self.set_head(node)

        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value

            if self.head != node:
                self.remove(node)
                self.set_head(node)
        else:
            new_node = Node(key, value)

            if self.capacity == 0:
                print("please send cache capacity > 0")
                return -1

            if self.current_size == self.capacity:
                del self.hash_map[self.end.key]  # delete the oldest
                self.remove(self.end)

            self.set_head(new_node)
            self.hash_map[key] = new_node

    def set_head(self, node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.current_size += 1

    def remove(self, node):
        if not self.head:
            return

        # removing the node and update pointers
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if not node.next and not node.prev:
            self.head = None
            self.end = None

        # if the node being removed is the one at the end, update the new end
        if self.end == node:
            self.end = node.next
            self.end.prev = None
        self.current_size -= 1
        return node

    def print_cache(self):
        n = self.head
        print("[head = %s, end = %s]" % (self.head, self.end), end=" ")
        while n:
            print("%s -> " % (n), end="")

            n = n.prev
        print("NULL")


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print("get(1) should return 1")
print(our_cache.get(1))  # returns 1

print("\nnow print cache")
our_cache.print_cache()

print("\nget(2) should return 2")
print(our_cache.get(2))  # returns 2

print("\nget(9) should return -1")
print(our_cache.get((9)))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.set(7, 7)

print("\nget(3) should return -1")
print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("\nprint cache again")
our_cache.print_cache()

print(our_cache.get(7))
print(our_cache.get(1))

our_cache = LRU_Cache(0)

our_cache.set(1, 1);
our_cache.set(2, 2);

print("\nget(1) should return -1\n")
print(our_cache.get(1))  # returns 1-

print("\nnow print cache\n")
our_cache.print_cache()

our_cache = LRU_Cache(1)

our_cache.set(1, 1);
our_cache.set(2, 2);

print("\nget(1) should return -1\n")
print(our_cache.get(1))  # returns -1

print("\nnow print cache\n")
our_cache.print_cache()

print("\nget(2) should return 2\n")
print(our_cache.get(2))  # returns 2

print("\nnow print cache\n")
our_cache.print_cache()


# the above test cases should print the following:
"""
get(1) should return 1
1

now print cache
[head = (1, 1), end = (2, 2)] (1, 1) -> (4, 4) -> (3, 3) -> (2, 2) -> NULL

get(2) should return 2
2

get(9) should return -1
-1

get(3) should return -1
-1

print cache again
[head = (7, 7), end = (1, 1)] (7, 7) -> (6, 6) -> (5, 5) -> (2, 2) -> (1, 1) -> NULL
7
1
please send cache capacity > 0
please send cache capacity > 0

get(1) should return -1

-1

now print cache

[head = None, end = None] NULL

get(1) should return -1

-1

now print cache

[head = (2, 2), end = (2, 2)] (2, 2) -> NULL

get(2) should return 2

2

now print cache

[head = (2, 2), end = (2, 2)] (2, 2) -> NULL


"""