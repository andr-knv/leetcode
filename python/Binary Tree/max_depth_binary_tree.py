from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# DFS Iterative
class SolutionOne:
    def maxDepth(self, root):
        if not root:
            return 0
    
        depth = 1
        stack = [[root, 1]]
        while stack:
            node, level = stack.pop()
            if node:
                depth = max(depth, level)
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])
        return depth      


# BFS
class SolutionTwo:
    def maxDepth(self, root) :
        if not root:
            return 0
    
        level = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.pop()

                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            level += 1
        return level


# DFS Recursive
class SolutionThree:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))