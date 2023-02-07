from TreeHelper import TreeNode


class BSTreeError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class BSTree:
    def __init__(self, root=None):
        if isinstance(root, TreeNode) or root is None:
            self.__root = root
        else:
            raise BSTreeError("The root should be a TreeNode class instance or a None", root)

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        if isinstance(value, TreeNode) or value is None:
            self.__root = value
        else:
            raise BSTreeError("The root should be a TreeNode class instance or a None", value)

    @staticmethod
    def subtree_elems(subroot):
        if subroot is not None:
            return BSTree.subtree_elems(subroot.left) + [subroot.value] + BSTree.subtree_elems(subroot.right)
        else:
            return []

    def sorted_elems(self):
        return self.subtree_elems(self.__root)

    def tree_search(self, value):
        x = self.__root
        while x is not None and value != x.value:
            if value < x.value:
                x = x.left
            else:
                x = x.right
        return x

    def tree_min(self):
        x = self.__root
        while x.left is not None:
            x = x.left
        return x

    def tree_max(self):
        x = self.__root
        while x.right is not None:
            x = x.right
        return x

    @staticmethod
    def subtree_min(subroot):
        x = subroot
        while x.left is not None:
            x = x.left
        return x

    @staticmethod
    def subtree_max(subroot):
        x = subroot
        while x.right is not None:
            x = x.right
        return x

    def insert(self, new_node):
        y = None
        x = self.__root
        while x is not None:
            y = x
            if new_node.value < x.value:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y is None:
            self.__root = new_node
        elif new_node.value < y.value:
            y.left = new_node
        else:
            y.right = new_node

    def __transplant(self, u, v):
        if u.parent is None:
            self.__root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, del_node):
        if del_node.left is None:
            self.__transplant(del_node, del_node.right)
        elif del_node.right is None:
            self.__transplant(del_node, del_node.left)
        else:
            y = self.subtree_min(del_node.right)
            if y.parent != del_node:
                self.__transplant(y, y.right)
                y.right = del_node.right
                y.right.parent = y
            self.__transplant(del_node, y)
            y.left = del_node.left
            y.left.parent = y


bst1 = BSTree(TreeNode(value=15))
print(bst1.sorted_elems())
bst1.insert(TreeNode(10))
bst1.insert(TreeNode(10))
print(bst1.tree_search(10).right.value)
print(bst1.sorted_elems())
bst1.insert(TreeNode(20))
print(bst1.sorted_elems())
bst1.delete(bst1.root)
print(bst1.sorted_elems())
bst1.delete(bst1.root)
print(bst1.sorted_elems())


