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




