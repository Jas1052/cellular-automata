import math

# returns array with indices of x-values of sorted t
def sort_i_x(t):
    pass
# returns array with indices of y-values of sorted t
def sort_i_y(t):
    pass
# returns value with distance^2 of two points; typically. This is not a distance function
#   since it is an unnecessary operation. using d^2 vs d will give the same desired distance 
#   weights. However, finding d uses the root function. 
def distanceWeight(u,v):
    dx = u[0] - v[0]
    dy = u[1] - v[1]
    return dx*dx + dy*dy

# returns indices of closest points; recursive
#   Algorithm described on GeeksForGeeks.com
#   1) Points sorted according to x values
#   2) Divide all points into two halves
#   3) Recursively find the smallest distances in boths ubarrays
#   4) Take the minimum of two smallest distances. Let the minimum be d
#   5) Finds all points that are at most distance away from largest dividing line
#   6) Find smallest distance among those points
#   7) Find the smallest distance between that distance the the ones from the divded halves
def search(i,j, i_x, i_y, t):        
    pass
 
def closest_pair(t):
    pass
