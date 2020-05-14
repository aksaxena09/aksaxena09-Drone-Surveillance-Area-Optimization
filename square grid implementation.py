from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon, Point
import matplotlib.tri as mtri
import numpy as np
from time import time
import matplotlib.path as mpltPath
from shapely.geometry import Polygon
from shapely.ops import nearest_points

xfig = np.asarray([-1.7, -1.7, 1.7, 1.7, -1.7])
yfig = np.asarray([-1.7, 1.7, 1.7, -1.7, -1.7])

#xfig = np.asarray([0.7, 0.7, 5.7, 5.7, 0.7])
#yfig = np.asarray([0.7, 5.7, 5.7, 0.7, 0.7])

#xfig = np.asarray([1, 0, 3.7, 5.7, 4.7, 1])
#yfig = np.asarray([0, 5.7, 7.7, 4.7, 1, 0])

#xfig = np.asarray([1, -1, 0, 3.7, 5.7, 4.7, 1])
#yfig = np.asarray([0, 3, 5.7, 7.7, 4.7, 1, 0])

polygon1=np.vstack((xfig, yfig)).T
polygon1=np.vstack((xfig, yfig)).T
xi, yi = np.meshgrid(np.linspace(-4, 8.25, 15), np.linspace(-4,8.25, 15))
fig, axs = plt.subplots(nrows=1, ncols=1)
axs.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
axs.plot(xfig, yfig)
axs.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
axs.set_title("Square Grid")
fig.tight_layout()
plt.show()

x1=xi.flatten()
y1=yi.flatten()
combined = np.vstack((x1, y1)).T
centroid = np.vstack((x1, y1)).T

for i in range(0, 210):
  if (i-14)%15==0:
      centroid[i][0]=0
      centroid[i][1]=0
  else:   
    centroid[i][0]=(combined[i][0]+combined[i+1][0])/2
    centroid[i][1]=(combined[i][1]+combined[i+15][1])/2

start_time = time()
path = mpltPath.Path(polygon1)
inside2 = path.contains_points(combined)
inside4 = path.contains_points(centroid)
inside5 = path.contains_points(centroid)

for j in range (0,209): 
  if (j-14)%15==0:
    inside5[j]=False
  else:
    po1 = Polygon(polygon1)
    p2 = Polygon([combined[j], combined[j+1], combined[j+16], combined[j+15], combined[j]])
    inside5[j]=po1.intersects(p2)
    
final_coordinates=[]
for i in range (0,209):
  if inside2[i]==True:
    final_coordinates.append(Point(combined[i]))

for i in range (0,209):
  poly=Polygon(polygon1)
  p1=0
  if inside5[i]==True:
    
    b1x=(combined[i][0]+combined[i+1][0])/2
    b1y=(combined[i][1]+combined[i+1][1])/2
    b2x=(combined[i+1][0]+combined[i+16][0])/2
    b2y=(combined[i+1][1]+combined[i+16][1])/2
    b3x=(combined[i+15][0]+combined[i+16][0])/2
    b3y=(combined[i+15][1]+combined[i+16][1])/2
    b4x=(combined[i+15][0]+combined[i][0])/2
    b4y=(combined[i+15][1]+combined[i][1])/2

    v1=Polygon([[b1x,b1y], combined[i], [b4x,b4y], centroid[i], [b1x,b1y]])
    v2=Polygon([[b2x,b2y], combined[i+1], [b1x,b1y], centroid[i], [b2x,b2y]])
    v3=Polygon([[b3x,b3y], combined[i+16], [b2x,b2y], centroid[i], [b3x,b3y]])
    v4=Polygon([[b4x,b4y], combined[i+15], [b3x,b3y], centroid[i], [b4x,b4y]])

    if poly.intersects(v1)==True:
      if inside2[i]==False:        
        point = Point(centroid[i])
        # The points are returned in the same order as the input geometries:
        p1, p2 = nearest_points(poly, point)
               
    if poly.intersects(v2):
      if inside2[i+1]==False:
        point = Point(centroid[i])
        # The points are returned in the same order as the input geometries:
        p1, p2 = nearest_points(poly, point)
        
    if poly.intersects(v3):
      if inside2[i+16]==False :
        point = Point(centroid[i])
        # The points are returned in the same order as the input geometries:
        p1, p2 = nearest_points(poly, point)

    if poly.intersects(v4):
      if inside2[i+15]==False :
        point = Point(centroid[i])
        # The points are returned in the same order as the input geometries:
        p1, p2 = nearest_points(poly, point)
    
    if p1!=0:
      final_coordinates.append(p1)
      #print(p1)
      #print(i)

duplicatearea=0
for i in range (0, 188):
  if inside5[i]==True:
    if inside2[i]==True and inside2[i+1]==True and inside2[i+15]==True and inside2[i+16]==True:
      duplicatearea=duplicatearea+4.28
    if inside2[i]==True and inside2[i+1]==True and inside2[i+15]==False and inside2[i+16]==True:
      duplicatearea=duplicatearea+(4.28/2)
    if inside2[i]==True and inside2[i+1]==False and inside2[i+15]==True and inside2[i+16]==True:
      duplicatearea=duplicatearea+(4.28/2)
    if inside2[i]==False and inside2[i+1]==True and inside2[i+15]==True and inside2[i+16]==True:
      duplicatearea=duplicatearea+(4.28/2)
    if inside2[i]==True and inside2[i+1]==True and inside2[i+15]==True and inside2[i+16]==False:
      duplicatearea=duplicatearea+(4.28/2)
    if inside2[i]==False and inside2[i+1]==False and inside2[i+15]==True and inside2[i+16]==True:
      duplicatearea=duplicatearea+(4.28/4)
    if inside2[i]==True and inside2[i+1]==False and inside2[i+15]==True and inside2[i+16]==False:
      duplicatearea=duplicatearea+(4.28/4)
    if inside2[i]==True and inside2[i+1]==True and inside2[i+15]==False and inside2[i+16]==False:
      duplicatearea=duplicatearea+(4.28/4)
    if inside2[i]==False and inside2[i+1]==True and inside2[i+15]==False and inside2[i+16]==True:
      duplicatearea=duplicatearea+(4.28/4)

waste_area=0

for i in range (0,209):
  poly=Polygon(polygon1)
 
  if inside2[i]==True:
    if inside4[i]==True and inside4[i-1]==True and inside4[i-15]==True and inside4[i-16]==True:
      waste_area=waste_area
    if inside4[i]==True and inside4[i-1]==True and inside4[i-15]==True and inside4[i-16]==False:
      waste_area=waste_area+(3.14/4)
    if inside4[i]==True and inside4[i-1]==True and inside4[i-15]==False and inside4[i-16]==True:
      waste_area=waste_area+(3.14/4)
    if inside4[i]==True and inside4[i-1]==False and inside4[i-15]==True and inside4[i-16]==True:
      waste_area=waste_area+(3.14/4) 
    if inside4[i]==False and inside4[i-1]==True and inside4[i-15]==True and inside4[i-16]==True:
      waste_area=waste_area+(3.14/4)    
    if inside4[i]==True and inside4[i-1]==True and inside4[i-15]==False and inside4[i-16]==False:
      waste_area=waste_area+(3.14/2)          
    if inside4[i]==False and inside4[i-1]==True and inside4[i-15]==False and inside4[i-16]==True:
      waste_area=waste_area+(3.14/2)          
    if inside4[i]==True and inside4[i-1]==False and inside4[i-15]==True and inside4[i-16]==False:
      waste_area=waste_area+(3.14/2)          
    if inside4[i]==False and inside4[i-1]==False and inside4[i-15]==True and inside4[i-16]==True:
      waste_area=waste_area+(3.14/2)          
    if inside4[i]==True and inside4[i-1]==False and inside4[i-15]==False and inside4[i-16]==False:
      waste_area=waste_area+(3.14*3/4)          
    if inside4[i]==False and inside4[i-1]==True and inside4[i-15]==False and inside4[i-16]==False:
      waste_area=waste_area+(3.14*3/4)          
    if inside4[i]==False and inside4[i-1]==False and inside4[i-15]==True and inside4[i-16]==False:
      waste_area=waste_area+(3.14*3/4)          
    if inside4[i]==False and inside4[i-1]==False and inside4[i-15]==False and inside4[i-16]==True:
      waste_area=waste_area+(3.14*3/4)          
    

  
      
      
q=1
x=0
for i in final_coordinates:
  print(q,i)
  q=q+1
  x=x+1
print("No. of Drones Required", x)
print("Minimum duplicate area", duplicatearea, "R*R sq units")
print("Minimum waste area", waste_area, "R*R sq units")
