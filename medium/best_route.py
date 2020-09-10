
# Returns the the maximum depart/return value <= max_distance
# If no such pair exists return [-1, -1]
def bestRoute(departs, returns, max_distance):
  returns = set(returns)
  departs = set(departs)
  optimal_dist = -1
  indicies = [-1,-1]
  for dist in departs:
    complement = max_distance - dist
    while complement > 0:
      if complement in returns:
        if complement + dist <= max_distance and complement+dist > optimal_dist:
          optimal_dist = complement + dist
          indicies = [dist, complement]
      complement -= 1
  return indicies

a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6]

print(bestRoute(a,b,7))
