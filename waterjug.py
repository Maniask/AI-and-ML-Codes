# Program to implement Water Jug Problem.
# Created By: Mani Agarwal
# Email : agarwalmani22@gmail.com
# Date  : 20-02-2020

jugs = [0,0]
queue = []

over = []
counter = 1
queue.append(jugs)
Jug1 = int(input("Jug 1: "))
Jug2 = int(input("Jug 2: "))
left = int(input("Final in jug 1: " ))

def Solve(queue, counter):
	jugs = queue.pop(0)
	over.append(jugs)

	counter += 1
	if (jugs[0] == left and jugs[1] == 0):
		print ("Solution found!")
		print ("Approx count: ", counter)
		return
	ApplyRule(jugs, queue)
	Solve(queue, counter)

def Append(queue, temporary):
	if not (temporary in queue) and not (temporary in over):
		queue.append(temporary)

	
def ApplyRule(jugs, queue):

	x = jugs[0]
	y = jugs[1]
	
	if x < Jug1: 
		print ("1")
		Append(queue, [Jug1,y])
		
	if y < Jug2: 
		print ("2")
		Append(queue, [x,Jug2])
		
	if x > 0: 
		print( "3")
		Append(queue, [0,y])
		
	if y > 0: 
		print ("4")
		Append(queue, [x,0])
	
	if x + y >= Jug1 and y > 0: 
		print ("5")
		Append(queue, [Jug1,y-Jug1+x])
		
		
	if x + y <= Jug1 and y > 0: 
		print ("6")
		Append(queue, [x+y,0])
		

	if x == 0 and y == left: 
		print ("7")
		Append(queue, [left,0])	
	
Solve(queue,0)