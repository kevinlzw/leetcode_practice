# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        lst = []
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node:
                lst.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else:
                lst.append("null")
        return ' '.join(lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        lst = data.split()
        if not lst:
            return None
        idx = 1
        deq = deque()
        root = TreeNode(lst[0])
        deq.append(root)
        while idx <= len(lst) - 1:
            node = deq.popleft()
            if lst[idx] != "null":
                node.left = TreeNode(lst[idx])
                deq.append(node.left)
            idx += 1
            if idx == len(lst):
                break
            if lst[idx] != "null":
                node.right = TreeNode(lst[idx])
                deq.append(node.right)
            idx += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))