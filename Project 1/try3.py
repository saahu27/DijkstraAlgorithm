import numpy as np
import matplotlib.pyplot as plt
import pylab

# def ObstacleMap():
# 	plot_x = []
# 	plot_y =[]
# 	obs_map = np.zeros((400,250))

# 	for x in range (0,400) :
# 		for y in range(0,250):

# 			l1 = y - ((0.316) *x) - 173.608  
# 			l2 = y + (1.23 * x) - 229.34 
# 			l3 = y + (3.2 * x) - 436 
# 			l4 = y - 0.857*x - 111.42 

# 			c = (x - 300)**2 + (y - 185)**2 - (40)**2 

# 			h1 = y - 0.57*x - 24.97 
# 			h2 = y + 0.577*x - 255.82
# 			h3 = x - 235 
# 			h6 = x - 165 
# 			h5 = y + 0.577*x - 175 
# 			h4 = y - 0.577*x + round(55.82) 

# 			if (l1<0 and l2>0 and l3<0 and l4>0) or (c<=0) or (h1<0 and h2<0 and h3<0 and h6>0 and h5>0 and h4>0):
# 				obs_map[x][y] = 1
# 				plot_x.append(x)
# 				plot_y.append(y)

# 	for i in range(400):
# 		plot_x.append(i)
# 		plot_y.append(0)
# 		obs_map[i][0] = 1

# 	for i in range(400):
# 		plot_x.append(i)
# 		plot_y.append(250)
# 		obs_map[i][249] = 1
# 	for i in range(250):
# 		plot_x.append(0)
# 		plot_y.append(i)
# 		obs_map[0][i] = 1
# 	for i in range(250):
# 		plot_x.append(400)
# 		plot_y.append(i)
# 		obs_map[399][i] = 1

# 	pylab.plot(plot_x,plot_y,".k")
# 	pylab.ylim((0,250))
# 	pylab.xlim((0,400))
# 	plt.plot(plot_x,plot_y,".k")
# 	plt.ylim((0,250))
# 	plt.xlim((0,400))
# 	plt.show()
# 	return plot_x, plot_y, obs_map

# x = ObstacleMap()

x = np.zeros((400,250))
s = x.shape
print(s[0],s[1])