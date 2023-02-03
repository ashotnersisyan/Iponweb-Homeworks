from TreeHelper import TreeNode


class TreeNodeError(Exception):
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
            raise TreeNodeError("The root should be a TreeNode class instance or a None", root)

    def Transplant(self, u, v):





