from TreeHelper import RBTreeNode


class RBTreeError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class RBTree:
    def __init__(self):
        self.__NULL = RBTreeNode(0)
        self.__NULL.color = 0
        self.__NULL.left = None
        self.__NULL.right = None
        self.root = self.__NULL

    @property
    def NULL(self):
        return self.__NULL

    def insert(self, key):
        node = RBTreeNode(key)
        node.parent = None
        node.value = key
        node.left = self.__NULL
        node.right = self.__NULL
        node.color = 1

        y = None
        x = self.root

        while x != self.__NULL:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def LR(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def RR(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.RR(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.LR(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.LR(x.parent)
                    s = x.parent.right
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.RR(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.LR(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.RR(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.LR(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.RR(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_node_helper(self, node, key):
        z = self.NULL
        while node != self.NULL:
            if node.value == key:
                z = node

            if node.value <= key:
                node = node.right
            else:
                node = node.left

        if z == self.NULL:
            print("The given value is not found in the Tree.")
            return

        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.fix_delete(x)

    def delete_node(self, val):
        self.delete_node_helper(self.root, val)

    def __printCall(self, node, indent, last):
        if node != self.NULL:
            print(indent, end=' ')
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.value) + "(" + s_color + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    def print_tree(self):
        self.__printCall(self.root, "", True)


bst = RBTree()
bst.insert(10)
bst.insert(20)
bst.insert(30)
bst.insert(5)
bst.insert(4)
bst.insert(2)
bst.print_tree()

print("\n After deleting.")
bst.delete_node(2)
bst.print_tree()
