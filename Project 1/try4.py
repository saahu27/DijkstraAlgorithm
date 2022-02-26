import sys
import os
import argparse
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
import heapq



class Node:

	def __init__(self, x, y, cost, parent_id):

		self.x = x
		self.y = y
		self.cost = cost
		self.parent_id = parent_id
	
	def __lt__(self,other):
		return self.cost < other.cost



def Actionmove_right(x,y,cost):
	x = x + 1
	cost = 1 + cost
	return x,y,cost

def Actionmove_left(x,y,cost):
	x = x - 1
	cost = 1 + cost
	return x,y,cost

def Actionmove_up(x,y,cost):
	y = y + 1
	cost = 1 + cost
	return x,y,cost

def Actionmove_down(x,y,cost):
	y = y - 1
	cost = 1 + cost
	return x,y,cost

def Actionmove_upright(x,y,cost):
	x = x + 1
	y = y + 1
	cost = 1 + cost
	return x,y,cost

def Actionmove_upleft(x,y,cost):
	x = x - 1
	y = y + 1
	cost = np.sqrt(2) + cost
	return x,y,cost

def Actionmove_downright(x,y,cost):
	x = x + 1
	y = y - 1
	cost = np.sqrt(2) + cost
	return x,y,cost

def Actionmove_downleft(x,y,cost):
	x = x -1
	y = y - 1
	cost = np.sqrt(2) + cost
	return x,y,cost

def Next_Node(move,x,y,cost):

	if move == 'Left':
		return Actionmove_left(x,y,cost)
	elif move == 'Right':
		return Actionmove_right(x,y,cost)
	elif move == 'Up':
		return Actionmove_up(x,y,cost)
	elif move == 'Down':
		return Actionmove_down(x,y,cost)
	elif move == 'UpRight':
		return Actionmove_upright(x,y,cost)
	elif move == 'UpLeft':
		return Actionmove_upleft(x,y,cost)
	elif move == 'DownRight':
		return Actionmove_downright(x,y,cost)
	elif move == 'DownLeft':
		return Actionmove_downleft(x,y,cost)
	else:
		return None

def ObstacleMap(width,height):

	# obstacle_map = np.full((width,height),np.inf)
	obstacle_map = np.zeros((width,height))

	for x in range(0,width) :
		for y in range(0,height):

			l1 = y - ((0.316) *x) - 173.608  
			l2 = y + (1.23 * x) - 229.34 
			l3 = y + (3.2 * x) - 436 
			l4 = y - 0.857*x - 111.42 

			c = (x - 300)**2 + (y - 185)**2 - (40)**2 

			h1 = y - 0.57*x - 24.97 
			h2 = y + 0.577*x - 255.82
			h3 = x - 235 
			h6 = x - 165 
			h5 = y + 0.577*x - 175 
			h4 = y - 0.577*x + 55.82 

			if (l1<0 and l2>0 and l3<0 and l4>0) or (c<=0) or (h1<0 and h2<0 and h3<0 and h6>0 and h5>0 and h4>0):
				obstacle_map[x][y] = -1

	return obstacle_map


def is_goal(current, goal):

	if (current.x == goal.x) and (current.y == goal.y):
		return True
	else:
		return False


def is_valid(x, y, obstacle_map):

	s = obstacle_map.shape

	if( x > s[0] or x < 0 or y > s[1] or y < 0 ):
		return False
	
	else:
		try:
			if(obstacle_map[x][y] == -1):
				return False
		except:
			pass
	return True

def Dijkstra_algorithm(start_node, goal_node,obstacle_map):

	if is_goal(start_node, goal_node):
		return None,1
	goal_node = goal_node
	actions = ['Left', 'Right','Up','Down','UpRight','UpLeft','DownRight','DownLeft']
	open_nodes = {}
	open_nodes[(start_node.x + start_node.y)* 500] = start_node
	closed_nodes = {}
	open_nodes_list = []  #this is also a opennode, created for use in while loop
	all_nodes = []
	heapq.heappush(open_nodes_list, [start_node.cost, start_node])

	while (len(open_nodes_list) != 0):

		current_node = (heapq.heappop(open_nodes_list))[1]
		all_nodes.append([current_node.x, current_node.y])
		current_id = (current_node.x + current_node.y) * 500

		if is_goal(current_node, goal_node):
			goal_node.parent_id = current_node.parent_id
			goal_node.cost = current_node.cost
			print("Goal Node found")
			return all_nodes,1

		if current_id in closed_nodes:   #need to check
			continue
		else:
			closed_nodes[current_id] = current_node
		
		del open_nodes[current_id]

		for move in actions:
			x,y,cost = Next_Node(move,current_node.x,current_node.y,current_node.cost)

			new_node = Node(x,y,cost,current_node)  #currentnode or currentnode id check

			new_node_id = (new_node.x + new_node.y) * 500

			if is_valid(new_node.x, new_node.y, obstacle_map) == False:
				continue
			elif new_node_id in closed_nodes:
				continue

			if new_node_id in open_nodes:
				if new_node.cost < open_nodes[new_node_id].cost:
					open_nodes[new_node_id].cost = new_node.cost
					open_nodes[new_node_id].parent_id = new_node.parent_id
			else:
				open_nodes[new_node_id] = new_node
			
			heapq.heappush(open_nodes_list, [ open_nodes[new_node_id].cost, open_nodes[new_node_id]])

	return  all_nodes,0

def Generate_Path(goal_node):  
	x_path = []
	y_path = []
	x_path.append(goal_node.x)
	y_path.append(goal_node.y)

	parent = goal_node.parent_id
	while parent != -1:
		x_path.append(parent.x)
		y_path.append(parent.y)
		parent = parent.parent_id
	
	return x_path,y_path


def plot(obstacle_map,x_path,y_path,all_nodes):

	obstacle_map = obstacle_map.astype(np.uint8)*255
	obstacle_map = np.dstack([obstacle_map, obstacle_map, obstacle_map])
	obstacle_map = cv2.flip(obstacle_map, 0)
	for i in range(len(all_nodes)):
		obstacle_map[251 - int(all_nodes[i][1]), int(all_nodes[i][0]), 0:3] = 251
		obstacle_map[251 - int(all_nodes[i][1]), int(all_nodes[i][0]), 0:3].astype(np.uint8)
		cv2.imshow("image", obstacle_map)
		cv2.waitKey(1)
	
	x_path.reverse()
	y_path.reverse()
	
	for i in range(len(x_path)):

		obstacle_map[201 - int(y_path[i]), int(x_path[i]), 0:3] = (255, 0,0)
		obstacle_map[201 - int(y_path[i]), int(x_path[i]), 0:3].astype(np.uint8)
		cv2.imshow("image", obstacle_map)
		cv2.waitKey(0)

if __name__ == '__main__':

	# radius = input("Enter Robot radius: ")
	# clearance = input("Enter clearance value: ")
	# radius = int(radius)
	# clearance = int(clearance)
	width = 400
	height = 250
	obstacle_map = ObstacleMap(width, height)

	start_coord = input("Enter start coordinates: ")
	start_x, start_y = start_coord.split()
	start_x = int(start_x)
	start_y = int(start_y)
	if not is_valid(start_x, start_y, obstacle_map):
		print("INVALID start node.")
		exit(-1)
	
	goal_coordinates = input("Enter start coordinates: ")
	goal_x, goal_y = goal_coordinates.split()
	goal_x = int(goal_x)
	goal_y = int(goal_y)
	if not is_valid(goal_x, goal_y, obstacle_map):
		print("INVALID goal node.")
		exit(-1)
	
	start_node = Node(start_x, start_y, 0.0, -1)
	goal_node = Node(goal_x, goal_y, 0.0, -1)
	all_nodes,flag = Dijkstra_algorithm(start_node, goal_node,obstacle_map)

	if (flag):
		x_path,y_path = Generate_Path(goal_node)
	else:
		print("not found")
		exit(-1)
	plot(obstacle_map,x_path,y_path,all_nodes)
	
	



	








