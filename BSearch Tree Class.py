### Tree node class###

class Tree_node():
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.left=None
        self.right=None
      
    def __repr__(self):
        return "[" + str(self.left) + \
               " (" + str(self.key) + "," + str(self.val) + ") " \
               + str(self.right) + "]"

### Binary search tree  ###
class BSearch_tree():
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        """ Insert element to BSearch_tree """
        def helper_insert(node, key, val):
            if node is None:
                return Tree_node(key, val)
            elif node.key == key:
                node.val = val
            elif node.key < key:
                node.right = helper_insert(node.right, key, val)
            else:
                node.left = helper_insert(node.left, key, val)
            return node
        self.root = helper_insert(self.root, key, val)

    def lookup(self,key):
        """ Search element to BSearch_tree """
        def helper_lookup(node, key):
            if node is None:
                return None
            elif key == node.key:
                return node.val
            elif node.key < key:
                return helper_lookup(node.right, key)
            return helper_lookup(node.left, key)
        return helper_lookup(self.root, key)

    def sum(self):
        """ Return sum of all elements in BSearch_tree """
        def helper_sum(node):
            if node is None:
                return 0
            return node.key + helper_sum(node.right) + helper_sum(node.left)
        return helper_sum(self.root)

    def find_closest_key(self, search_key):
        """ Return closest key to search_key in BSearch_tree """
        def helper_find_closest_key(node, search_key):
            if node is None:
                return None
            elif search_key == node.key:
                return node.key
            min_key = node.key
            min_sons = helper_find_closest_key(node.right \
                                               if node.key < search_key  \
                                               else node.left, search_key)
            if min_sons is not None \
               and abs(search_key-min_sons) < abs(search_key-min_key):
                min_key = min_sons
            return min_key
        return helper_find_closest_key(self.root, search_key)

    def is_balanced(self):
        """ Checks if BSearch_tree is balanced """
        def helper_is_balanced(node):
            if node is None:
                return True, 0
            right_balanced, right_height = helper_is_balanced(node.right)            
            left_balanced, left_height = helper_is_balanced(node.left)
            height = max(left_height, right_height) + 1
            is_balanced = right_balanced and left_balanced \
                          and abs(right_height - left_height) <= 1
            return is_balanced, height
        return helper_is_balanced(self.root)[0]
