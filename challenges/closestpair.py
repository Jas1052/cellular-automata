import math

# returns array with indices of x-values of sorted t
def sort_i_x(t):
    return [i for (i,u) in sorted(enumerate(t), key = lambda p: p[1][0])]

# returns array with indices of y-values of sorted t
def sort_i_y(t):
    return [i for (i,u) in sorted(enumerate(t), key = lambda p: p[1][1])]

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
    if i >= j:
        return None
    elif i + 1 == j:
        return (i_x[i], i_x[j])
    else: 
        k = (i + j) // 2
        left = search(i, k, i_x, i_y, t)
        right = search(k+1, j, i_x, i_y, t)

        # splitting into left and right based on min distance
        if left is None:
            (i_min, j_min) = right
        elif right is None:
            (i_min, j_min) = left
        else:
            (i_left, j_left) = left
            (i_right, j_right) = right
            d_left = distanceWeight(t[i_left], t[j_left])
            d_right = distanceWeight(t[i_right], t[j_right])
            # setting new min sections
            if d_left < d_right:
                (i_min, j_min) = (i_left, j_left)
            else:
                (i_min, j_min) = (i_right, j_right)
        # distance between closest points in left/right
        bestDistance = distanceWeight(t[i_min], t[j_min])

        # cutting area in half
        x = (t[i_x[k]][0] + t[i_x[k + 1]][0]) / 2

        area = [j for j in i_y if abs(t[j][0] - x) <= bestDistance]
        # for points in best section
        for index in range(len(area)):
            nextIndex = index + 1
            while nextIndex < len(area) and (t[i_y[nextIndex]][1] - t[i_y[index]][1]) < bestDistance and nextIndex - index <= 15:
                newDistance = distanceWeight(t[i_y[index]], t[i_y[nextIndex]])
                # check if new distance is smaller than closest in right/left
                if newDistance < bestDistance:
                    bestDistance = newDistance
                    i_min = index
                    j_min = nextIndex
                nextIndex = nextIndex + 1                  
        return (i_min, j_min)

# returns points from list and indices
def translate(t, indices):
    firstPoint = t[indices[0]]
    secondPoint = t[indices[1]]
    return "The closest points are " + str(firstPoint) + " and " + str(secondPoint)

# calls helper methods and search
def closest_pair(t):
    i_x = sort_i_x(t)
    i_y = sort_i_y(t)
    return search(0, len(t) - 1, i_x, i_y, t)

# points = [(1, 7)]
# points = [(0, 1), (3, 2), (2, 3)]
# points = [(0, 1), (3, 2), (2, 3), (7, 3), (4, 2)]
points = [(0, 1), (3, 2), (2, 3), (7, 3), (5, 2), (-1, -1), (-1, 0)]

# print(sort_i_x(points))
# print(sort_i_y(points))

print(translate(points, closest_pair(points)))