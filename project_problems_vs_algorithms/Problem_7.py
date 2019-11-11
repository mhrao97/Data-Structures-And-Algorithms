#  Problem 7: Request Routing in a Web Server with a Trie

"""
# HTTPRouter using a Trie

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the
Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching,
but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post"
and figure out what content to return. In a dynamic web server, the content will often come from a block of code
called a handler.

"""


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        # self.root = RouteTrieNode()
        self.root = "/"  # set to / since we are working with web addresses
        self.handler = None
        self.next = {}

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.next
        paths = paths.split("/")
        for path in paths:
            current.insert(RouteTrieNode(path))
            current = current.next[path]

        current.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if paths == "/":
            return self.handler

        paths = paths.split("/")

        for path in paths:
            current = self
            for child_path in path:
                current = current.next
                current = current[child_path]
            handler = current.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, value=""):
        # Initialize the node with children as before, plus a handler
        self.value = value
        self.handler = None
        self.next = {}

    def insert(self, next_path, handler=None):
        # Insert the node as before
        self.next[next_path] = self.next.get(next_path, RouteTrieNode(next_path))
        self.next[next_path].handler = handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = "/"
        self.handler = root_handler
        self.next = {}
        self.not_found = not_found_handler

    def add_handler(self, path, path_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path == self.root:
            self.handler = path_handler
        else:
            path = self.split_path(path)
            current = self.next
            x = True
            for child_path in path:
                if not child_path:
                    continue
                if x == True:
                    x = False
                    current[child_path] = current.get(child_path, RouteTrieNode(child_path))

                    current = current[child_path]
                else:
                    current.insert(child_path, path_handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        if path == "/":
            return self.handler
        path = self.split_path(path)
        current = self

        for child_path in path:
            if child_path:
                if child_path in current.next:
                    current = current.next
                    current = current[child_path]
                else:
                    return self.not_found

        handler = current.handler
        if handler:
            return handler
        else:
            return "None"

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split("/")


# Test cases
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print("\n----------test cases given in the problem------------")
print("/ should print root handler")
print(router.lookup("/")) # should print 'root handler'
print("\n/home should print 'not found handler' or None if you did not implement one")
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print("\n/home/about should print 'about handler'")
print(router.lookup("/home/about")) # should print 'about handler'
print("\n/home/about/ should print 'about handler'")
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print("\n/home/about/me should print 'not found handler'")
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print("\n-----edge case----")
print(router.lookup(""))
print(router.lookup(" "))

# the above test cases should print the following results
"""
----------test cases given in the problem------------
/ should print root handler
root handler

/home should print 'not found handler' or None if you did not implement one
None

/home/about should print 'about handler'
about handler

/home/about/ should print 'about handler'
about handler

/home/about/me should print 'not found handler'
not found handler

-----edge case----
root handler
not found handler

"""