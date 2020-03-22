# Program to implement graph.
# Created By: Mani Agarwal
# Email : agarwalmani22@gmail.com
# Date  : 20-02-2020


class Node(object):
    def __init__(self, missionaries_wrong_side, cannibals_wrong_side, boat_wrong_side):
        self.missionaries_wrong_side = missionaries_wrong_side
        self.cannibals_wrong_side = cannibals_wrong_side
        self.boat_wrong_side = boat_wrong_side
        self.missionaries_right_side = 3 - self.missionaries_wrong_side
        self.cannibals_right_side = 3 - self.cannibals_wrong_side
        self.parent = None
    
    def is_goal_state(self):
        if self.missionaries_wrong_side == 0 and self.cannibals_wrong_side == 0 and \
            self.boat_wrong_side == 0:
            return True
        else:
            return False
        
    def __eq__(self, other):
        return self.missionaries_wrong_side == other.missionaries_wrong_side and self.cannibals_wrong_side == other.cannibals_wrong_side \
                   and self.boat_wrong_side == other.boat_wrong_side and self.cannibals_right_side == other.cannibals_right_side \
                   and self.missionaries_right_side == other.missionaries_right_side

    def __hash__(self):
        return hash((self.missionaries_wrong_side, self.cannibals_wrong_side, self.boat_wrong_side, self.missionaries_right_side, \
               self.cannibals_right_side))         

         
    def permissible_state(self):
        
        if(self.missionaries_wrong_side < 0 or (self.cannibals_wrong_side < 0) or (self.missionaries_wrong_side > 3) or \
           (self.cannibals_wrong_side > 3) or (self.missionaries_right_side < 0) or (self.missionaries_right_side > 3) or \
           (self.cannibals_right_side < 0) or (self.cannibals_right_side > 3)):
            return False
        
        if (self.missionaries_wrong_side == 0 or (self.missionaries_wrong_side >= self.cannibals_wrong_side)) and \
              (self.missionaries_right_side == 0 or (self.missionaries_right_side >= self.cannibals_right_side)):
            return True
        else: 
            return False
        
    
    def get_current_state(self):
        return self.missionaries_wrong_side, self.cannibals_wrong_side, \
              self.boat_wrong_side
    
    def get_child_nodes(self, current_state):
        childNodes = []
        if self.boat_wrong_side == 1:
            # move two missionaries to right bank
            newNode = Node(self.missionaries_wrong_side-2, self.cannibals_wrong_side, 0)
            if newNode.permissible_state():
                newNode.parent = current_state
                #print("Parent: ", newNode.parent.get_current_state())
                childNodes.append(newNode)
                
            # move two cannibals to right bank
            newNode = Node(self.missionaries_wrong_side, self.cannibals_wrong_side-2, 0)
            if newNode.permissible_state():
                newNode.parent = current_state
                childNodes.append(newNode)
                
            # move one cannibal and one missionary to right bank
            newNode = Node(self.missionaries_wrong_side-1, self.cannibals_wrong_side-1, 0)
            if newNode.permissible_state():
                newNode.parent = current_state
                childNodes.append(newNode)
                
            # move one cannibal  to right bank
            newNode = Node(self.missionaries_wrong_side, self.cannibals_wrong_side-1, 0)
            if newNode.permissible_state():
                newNode.parent = current_state
                childNodes.append(newNode)
                
            # move one missionary to right bank
            newNode = Node(self.missionaries_wrong_side-1, self.cannibals_wrong_side, 0)
            if newNode.permissible_state():
                newNode.parent = current_state
                childNodes.append(newNode)
            
            
        else:
            # move two missionaries right to left
            newNode = Node(self.missionaries_wrong_side+2, self.cannibals_wrong_side, 1)
            if newNode.permissible_state():
                newNode.parent = current_state
                childNodes.append(newNode)
                
            # move two cannibals right to left
            newNode = Node(self.missionaries_wrong_side, self.cannibals_wrong_side+2, 1)
            if newNode.permissible_state():
                newNode.parent = current_state
                childNodes.append(newNode)
                
            # move one cannibal and one missionary right to left
            newNode = Node(self.missionaries_wrong_side+1, self.cannibals_wrong_side+1, 1)
            if newNode.permissible_state():
                newNode.parent = current_state
                childNodes.append(newNode)
                
            # move one cannibal right to left
            newNode = Node(self.missionaries_wrong_side, self.cannibals_wrong_side+1, 1)
            if newNode.permissible_state():
                newNode.parent = current_state
                childNodes.append(newNode)
                
            # move one missionary right to left
            newNode = Node(self.missionaries_wrong_side+1, self.cannibals_wrong_side, 1)
            if newNode.permissible_state():
                newNode.parent = current_state
                childNodes.append(newNode)
    
        return childNodes
            
        
    

class Game(object):
    def __init__(self):
        self.initial_node = Node(missionaries_wrong_side=3, cannibals_wrong_side=3, boat_wrong_side=1)
        
    def get_initial_node(self):
        return self.initial_node.missionaries_wrong_side, self.initial_node.cannibals_wrong_side, \
              self.initial_node.boat_wrong_side
              
       
    
    def breadth_first_search(self):
        if self.initial_node.is_goal_state():
            return self.initial_node
        frontier = list()
        visited = set()
        frontier.append(self.initial_node)
        
        while frontier:
            current_state = frontier.pop(0)
            print("current state: ", current_state.get_current_state())
            print(current_state.is_goal_state())
            if current_state.is_goal_state():
                return current_state
            
            visited.add(current_state)
            expand_current_state = current_state.get_child_nodes(current_state)
            for child in expand_current_state:
                if child not in frontier and child not in visited:
                    frontier.append(child)
        return "No solution found"
            
g = Game()
print("Initial node: ", g.initial_node.missionaries_wrong_side, g.initial_node.cannibals_wrong_side, \
      g.initial_node.boat_wrong_side)
goal_node = g.breadth_first_search()  
