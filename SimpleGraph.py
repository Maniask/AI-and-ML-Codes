# Program to implement graph.
# Created By: Mani Agarwal
# Email : agarwalmani22@gmail.com
# Date  : 20-02-2020

import sys

class graph:
    dict={}
    
    def menu(self):
            print("1. New node")
            print("2. New edge")
            print("3. Del a node")
            print("4: Del an edge")
            print("5. Print graph")
            print("6. Exit program")
                
    def select(self):
        choice = 10
        while(choice!=0):
            self.menu()
            choice=input()
            if choice == '1':
                self.add_node()
            if choice == '2':
                self.add_edge()
            if choice == '3':
                self.del_node()
            if choice == '4':
                self.del_edge()
            if choice == '5':
                self.show_graph()
                self.dfs()
            if choice == '6':
                sys.exit()
            else:
                pass
                print()
                
    def add_node(self):
        print("Enter node : ") 
        node=int(input())
        if node not in self.dict:
            self.dict[node]=[]
            print("Node addition successful...")
        else:
            print("Node already exists.")
            
    def add_edge(self):
        print("Enter node at which you want to add edge : ")
        n=int(input())
        print("Enter edge : ")
        e=int(input())
        if n in self.dict and e not in self.dict:
            self.dict[n].append(e)
            print("Edge insertion successful...")
        else:
            print("Invalid Input")
    
    def del_node(self):
        print("Enter node : ")
        n=int(input())
        if n in self.dict:
            for i in self.dict:
                for values in self.dict[i]:
                    if(values == n):
                        self.dict[i].remove(values)
            del self.dict[n]
            print("Deletion successful...")
        else:
            print("Node not found")
    
    def del_edge(self):
        print("Enter node from which you want to delete the edge : ")
        n=int(input())
        print("Enter edge : ")
        e=int(input())
        if n in self.dict and e in self.dict:
            self.dict[n].remove(e)
            print("Edge deletion successful...")
        else:
            print("Invalid Input")
            
    
    def show_graph(self):
        print(self.dict)

            
            
obj = graph()
obj.select()