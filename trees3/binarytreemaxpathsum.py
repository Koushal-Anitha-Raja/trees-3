

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #declaring a variable for maximum 
        self.maximum=root.val
        #only root is needed as parameter
        self.recur(root)
        return self.maximum
        
    def recur(self,root):
        #base condition
        if root==None:
            return 0
        #logic
        #finding the left of sub tree
        leftsum=max(self.recur(root.left),0)
        #finding the right of sub tree
        rightsum=max(self.recur(root.right),0)
        
        #calculating the rootmax
        rootmax=root.val+leftsum+rightsum
        
        #check whether the root max is greater than global maximum
        if self.maximum<rootmax:
            #then changing the global max to rootmax
            self.maximum=rootmax
            #else return the max plus left and right 
        return root.val + max(leftsum,rightsum)