

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

# x = 199
# y = 58
# width = 400
# height = 250
# obstacle_map = ObstacleMap(width,height)
# print(is_valid(x,y,obstacle_map))