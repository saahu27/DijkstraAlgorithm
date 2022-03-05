        # #Polygon Obstacle (clearance)
        # L1 = (y-5) - ((0.316) *(x+5)) - 173.608  
        # L2 = (y+5) + (1.23 * (x+5)) - 229.34 
        # L3 = (y-5) + (3.2 * (x-5)) - 436 
        # L4 = (y+5) - 0.857*(x-5) - 111.42 
        # L5 = y + (0.1136*x) - 189.09
        
        # #Circle Obstacle (clearance)
        # C = ((y -185)**2) + ((x-300)**2) - (40+5)**2  
            
        # #Hexagon Obstacle (clearance)
        # H1 = (y-5) - 0.577*(x+5) - 24.97
        # H2 = (y-5) + 0.577*(x-5) - 255.82
        # H3 = (x-6.5) - 235 
        # H6 = (x+6.5) - 165 
        # H5 = (y+5) + 0.577*(x+5) - 175 
        # H4 = (y+5) - 0.577*(x-5) + 55.82 
        
        # if(H1<0 and H2<0 and H3<0 and H4>0 and H5>0 and H6>0) or C<=0  or (L1<0 and L5>0 and L4>0)or (L2>0 and L5<0 and L3<0):
        #     obstacle_map[x,y]=1

        #     if(H1<h1 and H2<h2 and H3<h3 and H4>h4 and H5>h5 and H6>h6) or C>c or (L1<l1 and L5>l5 and L4>l4) or (L2>l2 and L5<l5 and L3<l3):
        #         x_clear.append(x)
        #         y_clear.append(y)