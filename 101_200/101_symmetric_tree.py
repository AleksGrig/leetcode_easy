# 101. Symmetric Tree

# Given the root of a binary tree,
# check whether it is a mirror of itself (i.e., symmetric around its center).


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(val=2, left=None, right=None),
        right=TreeNode(val=None, left=None, right=None),
    ),
    right=TreeNode(
        val=2,
        left=None,
        right=TreeNode(val=2, left=None, right=None),
    ),
)


# equality
def isSymmetric(root: TreeNode):
    def check(root1: TreeNode, root2: TreeNode):
        if root1 == None and root2 == None:
            return True
        elif root1 == None and root2 != None:
            return False
        elif root1 != None and root2 == None:
            return False
        else:
            if root1.val != root2.val:
                return False
            else:
                return check(root1.left, root2.left) and check(root1.right, root2.right)

    return check(root.left, root.right)


def isSymmetric1(root: TreeNode):
    l, r = [], []
    def left_traverse(root: TreeNode):
        if root != None:
            left_traverse(root.left)
            l.append(root.val)
            left_traverse(root.right)
    def right_traverse(root: TreeNode):
        if root != None:
            right_traverse(root.right)
            r.append(root.val)
            right_traverse(root.left)
    left_traverse(root.left)
    right_traverse(root.right)
    return l == r


print(isSymmetric1(root))
