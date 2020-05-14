from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon, Point
import matplotlib.tri as mtri
import numpy as np
from time import time
import matplotlib.path as mpltPath
from shapely.geometry import Polygon
from shapely.ops import nearest_points

x = np.asarray([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, ])

y = np.asarray([-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, 
                -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  
                 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
                 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,  
                 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ])

x1 = np.asarray([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
                -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5])

y1 = np.asarray([-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, 
                -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  
                 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
                 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,  
                 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, 
                -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  
                 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
                 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,  
                 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ])

xfig = np.asarray([-1.7, -1.7, 1.7, 1.7, -1.7])
yfig = np.asarray([-1.7, 1.7, 1.7, -1.7, -1.7])

#xfig = np.asarray([1, 0, 3.7, 5.7, 4.7, 1])
#yfig = np.asarray([0, 5.7, 7.7, 4.7, 1, 0])

#xfig = np.asarray([1, -1, 0, 3.7, 5.7, 4.7, 1])
#yfig = np.asarray([0, 3, 5.7, 7.7, 4.7, 1, 0])

polygon1=np.vstack((xfig, yfig)).T
combined = np.vstack((x, y)).T
centroid = np.vstack((x1, y1)).T


for i in range(0,188):
    z=i/14
    if i%14==0:
      centroid[i*2][0]=0
      centroid[i*2][1]=0
      centroid[(i*2)+1][0]=0
      centroid[(i*2)+1][1]=0   
    else:
      if (z%2)!=0 :
        centroid[i*2][0]=(combined[i][0]+combined[i+1][0]+combined[i+15][0])/3
        centroid[i*2][1]=(combined[i][1]+combined[i+1][1]+combined[i+15][1])/3
        centroid[(i*2)+1][0]=(combined[i][0]+combined[i+14][0]+combined[i+15][0])/3
        centroid[(i*2)+1][1]=(combined[i][1]+combined[i+14][1]+combined[i+15][1])/3
      
      elif (z%2)==0 :
        centroid[(i*2)+1][0]=(combined[i][0]+combined[i+1][0]+combined[i+15][0])/3
        centroid[(i*2)+1][1]=(combined[i][1]+combined[i+1][1]+combined[i+15][1])/3
        centroid[(i*2)][0]=(combined[i][0]+combined[i+14][0]+combined[i+15][0])/3
        centroid[(i*2)][1]=(combined[i][1]+combined[i+14][1]+combined[i+15][1])/3
  

triang = mtri.Triangulation(x, y)
fig = plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
ax.triplot(triang, 'k-')
ax.plot(xfig, yfig)
ax.set_title('Triangular Grid')
xrange = [-4, 10]
yrange = [-4, 10]
ax.set_xlim(*xrange)
#ax.set_xticks(list(*xrange)+ list([xrange[-1]]))
ax.set_ylim(*yrange)
#ax.set_yticks(range(*yrange) + [yrange[-1]])
ax.set_aspect(1)


start_time = time()
path = mpltPath.Path(polygon1)
inside2 = path.contains_points(combined)
inside4 = path.contains_points(centroid)
inside5 = path.contains_points(centroid)

for j in range (0,188):
  z=j/14
  if j%14==0:
    
    inside5[j*2]=False
    inside5[(j*2)+1]=False
  elif z%2!=0 :    
    po1 = Polygon(polygon1)
    p2 = Polygon([combined[j], combined[j+1], combined[j+15], combined[j]])
    p3 =  Polygon([combined[j], combined[j+14], combined[j+15], combined[j]])
    inside5[j*2]=po1.intersects(p2)
    inside5[(j*2)+1]=po1.intersects(p3)
  elif z%2==0 :
    po1 = Polygon(polygon1)
    p2 = Polygon([combined[j], combined[j+1], combined[j+15], combined[j]])
    p3 =  Polygon([combined[j], combined[j+14], combined[j+15], combined[j]])
    inside5[j*2]=po1.intersects(p3)
    inside5[(j*2)+1]=po1.intersects(p2)

final_coordinates=[]

for i in range (0,188):
  if inside2[i]==True:
    final_coordinates.append(Point(combined[i]))


for i in range (0,188):
  poly=Polygon(polygon1)
  p1=0
  if inside5[i*2]==True:
    #print(i)
    b1x=(combined[i][0]+combined[i+1][0])/2
    b1y=(combined[i][1]+combined[i+1][1])/2
    b2x=(combined[i+1][0]+combined[i+15][0])/2
    b2y=(combined[i+1][1]+combined[i+15][1])/2
    b3x=(combined[i][0]+combined[i+15][0])/2
    b3y=(combined[i][1]+combined[i+15][1])/2

    v1=Polygon([[b1x,b1y], combined[i], [b3x,b3y], centroid[i*2], [b1x,b1y]])
    v2=Polygon([[b2x,b2y], combined[i+1], [b1x,b1y], centroid[i*2], [b2x,b2y]])
    v3=Polygon([[b3x,b3y], combined[i+15], [b2x,b2y], centroid[i*2], [b3x,b3y]])
    #print(v1)
    #print(v2)
    #print(v3)

    if poly.intersects(v1):
      if inside2[i]==False:        
        point = Point(centroid[i*2])
        # The points are returned in the same order as the input geometries:
        p1, p2 = nearest_points(poly, point)
               
    if poly.intersects(v2):
      if inside2[i+1]==False:
        point = Point(centroid[i*2])
        # The points are returned in the same order as the input geometries:
        p1, p2 = nearest_points(poly, point)
        
    if poly.intersects(v3):
      if inside2[i+15]==False :
        point = Point(centroid[i*2])
        # The points are returned in the same order as the input geometries:
        p1, p2 = nearest_points(poly, point)
    
    
    if p1!=0:
      #p1=p1*2
      final_coordinates.append(p1)
      #print(p1)
     

  elif inside5[(i*2)+1]==True:
    #print(i)
    b1x=(combined[i][0]+combined[i+15][0])/2
    b1y=(combined[i][1]+combined[i+15][1])/2
    b2x=(combined[i+15][0]+combined[i+14][0])/2
    b2y=(combined[i+15][1]+combined[i+14][1])/2
    b3x=(combined[i+14][0]+combined[i][0])/2
    b3y=(combined[i+14][1]+combined[i][1])/2

    v1=Polygon([[b1x,b1y], combined[i], [b3x,b3y], centroid[i*2], [b1x,b1y]])
    v2=Polygon([[b2x,b2y], combined[i+1], [b1x,b1y], centroid[i*2], [b2x,b2y]])
    v3=Polygon([[b3x,b3y], combined[i+15], [b2x,b2y], centroid[i*2], [b3x,b3y]])
    #print(v1)
    #print(v2)
    #print(v3)
    if poly.intersects(v1):
      if inside2[i]==False:
        point = Point(centroid[(i*2)+1])
        # The points are returned in the same order as the input geometries:
        p1, p2 = nearest_points(poly, point)
        
       
    if poly.intersects(v2):
      if inside2[i+15]==False:
        point = Point(centroid[(i*2)+1])
        # The points are returned in the same order as the input geometries:
        p1, p2 = nearest_points(poly, point)
        
        
    if poly.intersects(v3):
      if inside2[i+14]==False:
        point = Point(centroid[(i*2)+1])
        # The points are returned in the same order as the input geometries:
        p1, p2 = nearest_points(poly, point)

   
    if p1!=0:
      #p1=p1*2
      final_coordinates.append(p1)
     # print(p1)

duplicatearea=0
for i in range (0, 188):
  if inside5[i*2]==True:
    if inside2[i]==True and inside2[i+1]==True and inside2[i+15]==True:
      duplicatearea=duplicatearea+3.17
    if inside2[i]==True and inside2[i+1]==True and inside2[i+15]==False:
      duplicatearea=duplicatearea+(3.17/3)
    if inside2[i]==True and inside2[i+1]==False and inside2[i+15]==True:
      duplicatearea=duplicatearea+(3.17/3)
    if inside2[i]==False and inside2[i+1]==True and inside2[i+15]==True:
      duplicatearea=duplicatearea+(3.17/3)
      
  if inside5[(i*2)+1]==True:
    if inside2[i]==True and inside2[i+14]==True and inside2[i+15]==True:
      duplicatearea=duplicatearea+3.17
    if inside2[i]==True and inside2[i+14]==True and inside2[i+15]==False:
      duplicatearea=duplicatearea+(3.17/3)
    if inside2[i]==True and inside2[i+14]==False and inside2[i+15]==True:
      duplicatearea=duplicatearea+(3.17/3)
    if inside2[i]==False and inside2[i+14]==True and inside2[i+15]==True:
      duplicatearea=duplicatearea+(3.17/3)

waste_area=0
for i in range (0, 188):
  check=0
  if inside2[i]==True:
    if inside4[i*2]==True:
      check=check+1
    if inside4[(i*2)+1]==True:
      check=check+1
    if inside4[(i-15)*2]==True:
      check=check+1
    if inside4[((i-15)*2)+1]==True:
      check=check+1
    if inside4[((i-16)*2)+1]==True:
      check=check+1
    if inside4[((i-1)*2)+1]==True:
      check=check+1
    
    waste_area=waste_area+((3.14*check)/4)

print(final_coordinates.pop)     
q=1
x=0
for i in final_coordinates:
  print(q,i)
  q=q+1
  x=x+1
print("No. of Drones Required", x)
print("Minimum duplicate area", duplicatearea, "sq units")
print("Minimum waste area", waste_area, "sq units")


