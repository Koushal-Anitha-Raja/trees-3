#TC: 0(N)
#SC:0(H)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #setting the flag to true
        self.flag=True
        self.recur(root)
        #returning the flaf variable 
        return self.flag
    
    def recur(self,root):
        #base condition
        if root==None:
            return 0
        
        #finding the left of sub tree
        leftht=self.recur(root.left)
        #finding the right of subtree
        rightht=self.recur(root.right)
        
        #logic if the difference value is greater than one return false 
        if abs(leftht-rightht)>1:
            #then change the flag to false
            self.flag=False
            
        #post order traversal where we are incrementing the value one at each level
        return 1+max(leftht,rightht)
        