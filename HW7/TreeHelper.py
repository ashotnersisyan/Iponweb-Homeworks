class TreeNodeError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class TreeNode:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.__value = value
        if isinstance(parent, TreeNode) or parent is None:
            self.__parent = parent
        else:
            raise TreeNodeError("The parent should be a TreeNode class instance or a None", parent)
        if isinstance(left, TreeNode) or left is None:
            self.__left = left
        else:
            raise TreeNodeError("The left child should be a TreeNode class instance or a None", left)
        if isinstance(right, TreeNode) or right is None:
            self.__right = right
        else:
            raise TreeNodeError("The right child should be a TreeNode class instance or a None", right)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value1):
        self.__value = value1

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if isinstance(value, TreeNode) or value is None:
            self.__parent = value
        else:
            raise TreeNodeError("The parent should be a TreeNode class instance or a None", value)

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        if isinstance(value, TreeNode) or value is None:
            self.__left = value
        else:
            raise TreeNodeError("The parent should be a TreeNode class instance or a None", value)

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        if isinstance(value, TreeNode) or value is None:
            self.__right = value
        else:
            raise TreeNodeError("The parent should be a TreeNode class instance or a None", value)


class RBTreeNodeError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class RBTreeNode:
    def __init__(self, value=None, color=1, parent=None, left=None, right=None):
        self.__value = value
        if color in (0, 1):
            self.__color = color
        else:
            raise RBTreeNodeError("The color should be 0 or 1", color)
        if isinstance(parent, RBTreeNode) or parent is None:
            self.__parent = parent
        else:
            raise RBTreeNodeError("The parent should be a TreeNode class instance or a None", parent)
        if isinstance(left, RBTreeNode) or left is None:
            self.__left = left
        else:
            raise RBTreeNodeError("The left child should be a TreeNode class instance or a None", left)
        if isinstance(right, RBTreeNode) or right is None:
            self.__right = right
        else:
            raise RBTreeNodeError("The right child should be a TreeNode class instance or a None", right)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value1):
        self.__value = value1

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if value in (0, 1):
            self.__color = value
        else:
            raise RBTreeNodeError("The color should be 0 or 1", value)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if isinstance(value, RBTreeNode) or value is None:
            self.__parent = value
        else:
            raise RBTreeNodeError("The parent should be a TreeNode class instance or a None", value)

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        if isinstance(value, RBTreeNode) or value is None:
            self.__left = value
        else:
            raise RBTreeNodeError("The parent should be a TreeNode class instance or a None", value)

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        if isinstance(value, RBTreeNode) or value is None:
            self.__right = value
        else:
            raise RBTreeNodeError("The parent should be a TreeNode class instance or a None", value)
