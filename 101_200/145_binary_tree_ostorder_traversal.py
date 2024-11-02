# 145. Binary Tree Postorder Traversal

# Given the root of a binary tree, return the postorder traversal of its nodes' values.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(
    1, left=None, right=TreeNode(2, left=TreeNode(3, left=None, right=None), right=None)
)


def postorderTraversal(root):
    ans = []

    def traverse(root):
        if root != None:
            traverse(root.left)
            traverse(root.right)
            ans.append(root.val)

    traverse(root)
    return ans


print(postorderTraversal(root))
