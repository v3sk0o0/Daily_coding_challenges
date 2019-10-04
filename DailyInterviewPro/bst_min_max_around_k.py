#  Given an integer k and a binary search tree, find the floor (less than or equal to) of k,
#  and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.


lass Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def max_min_none(*args):
    """
    max(None, int) ->  TypeError
    min(None, int) ->  TypeError
    helper function to  compare None to int
    """
    max_value = None
    min_value = None
    for pair in args:
        if pair[0] != None:
            if max_value == None:
                max_value = pair[0]
            else:
                max_value = max(max_value, pair[0])
        
        if pair[1] != None:
            if min_value == None:
                min_value = pair[1]
            else:
                min_value = min(min_value, pair[1])
    
    return (max_value, min_value)        
        
def findCeilingFloor(root_node, k, floor=None, ceil=None):
     
    if root_node == None:
        return (floor, ceil)
    
    if root_node.value == k:
        return (root_node.value, root_node.value)

    if root_node.value < k:
        # Can't compare directly None with integer
        floor = max(root_node.value, floor) if floor  else root_node.value

    #explicita- No need for this if statement
    if root_node.value > k:
        ceil = min(root_node.value, ceil) if ceil else root_node.value
        
    return max_min_none(findCeilingFloor(root_node.left, k, floor=floor, ceil=ceil), 
                        findCeilingFloor(root_node.right, k, floor=floor, ceil=ceil))

    # Fill this in.

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print (findCeilingFloor(root, 5))
