# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# IDEA: we do a binary search on the last layer to find the number of nodes in the last layer -> we find that number with a number of tries of  O(log(n/2)) = O(log(n))
# Each try costs O(log(n)) because from the root we have to reach the lowest layer
class Solution:
    def findDepth(self, root) -> int:
        if not root:
            return 0
        return 1 + self.findDepth(root.left)

    def check(self, root, path) -> bool:
        for i in path:
            if i == 0: 
                root = root.left
            else:
                root = root.right

        if root:
            return True
        else:
            return False


    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        depth = self.findDepth(root)

        # path = [0, 0, 1, 0, ...] -> 0 indicates to go left, 1 to go right
        path = [0 for _ in range(depth-1)]

        for i in range(len(path)):
            path[i] = 1
            present = self.check(root, path)
            if not present:
                path[i] = 0

        count = 2**(depth-1) - 1

        for i,x in enumerate(path[::-1]):
            count += x * 2**i

        count += 1

        return count
        
            