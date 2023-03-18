class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

class RouteTrie:
    def __init__(self, root_handler=None):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_parts, handler):
        node = self.root
        for part in path_parts:
            if part not in node.children:
                node.children[part] = RouteTrieNode()
            node = node.children[part]
        node.handler = handler

    def find(self, path_parts):
        node = self.root
        for part in path_parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler

class Router:
    def __init__(self, root_handler=None, not_found_handler=None):
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.trie.insert(path_parts, handler)

    def lookup(self, path):
        path_parts = self.split_path(path)
        handler = self.trie.find(path_parts)
        if handler is None:
            # Try again with a trailing slash
            handler = self.trie.find(path_parts + [''])
        if handler is None and self.not_found_handler is not None:
            handler = self.not_found_handler
        return handler

    def split_path(self, path):
        parts = path.strip('/').split('/')
        return [part for part in parts if part]

router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))